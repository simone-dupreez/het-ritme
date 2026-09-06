#!/usr/bin/env python3
"""
Het Ritme — Budget workbook builder.

Builds the full 9-screen budget planner workbook for one edition ("calm" or
"loud") per PLANNER-SPEC-BUDGET.md / BUILD-GUIDE.md / DESIGN-SYSTEM.md in
project/design_handoff_ritme_planners/. Reads shared tokens from
design-tokens.json.

Usage:
    python3 build_workbook.py calm
    python3 build_workbook.py loud
    python3 build_workbook.py            # builds both
"""
import json
import os
import sys

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Border, Side, Alignment, Protection
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import DataBarRule, CellIsRule, FormulaRule
from openpyxl.utils import get_column_letter
from openpyxl.workbook.defined_name import DefinedName
from openpyxl.worksheet.page import PageMargins

REPO_ROOT = "/home/claude/repo"
TOKENS_PATH = os.path.join(REPO_ROOT, "design-tokens.json")
OUT_DIR = os.path.join(REPO_ROOT, "build")

with open(TOKENS_PATH) as f:
    TOKENS = json.load(f)

# ---------------------------------------------------------------------------
# Palettes
# ---------------------------------------------------------------------------

def palette(edition):
    e = TOKENS["editions"][edition]
    ink = TOKENS["ink"]
    if edition == "calm":
        return {
            "ink": ink,
            "bodyInk": e["bodyInk"],
            "quietInk": e["quietInk"],
            "paper": e["bg"],
            "paperAlt": e["bgAlt"],
            "card": e["card"],
            "cellWhite": e["cellWhite"],
            "rule": e["rule"],
            "accent": e["accent"],
            "calcFill": e["calculatedFill"],
            "calcBorder": e["calculatedBorder"],
            "overLimit": e["overLimit"],
            "railCurrentFill": e["accent"],
            "railCurrentFont": TOKENS["paper"],
            "categoryColor": e["accent"],
        }
    else:
        return {
            "ink": ink,
            "bodyInk": e["bodyInk"],
            "quietInk": "#8A7F68",  # nearest quiet tone for Loud, not in tokens explicitly
            "paper": e["cream"],
            "paperAlt": e["track"],
            "card": e["cardCream"],
            "cellWhite": "#FFFFFF",
            "rule": e["calculatedBorder"],
            "accent": e["coral"],
            "calcFill": e["calculatedFill"],
            "calcBorder": e["calculatedBorder"],
            "overLimit": e["coral"],
            "railCurrentFill": e["coral"],
            "railCurrentFont": e["cream"],
            "categoryColor": e["coral"],
            "teal": e["teal"],
            "gold": e["gold"],
            "grape": e["grape"],
            "lime": e["lime"],
        }


def hexf(h):
    """openpyxl wants ARGB without '#'."""
    return "FF" + h.lstrip("#").upper()


SHEET_NAMES = [
    "1 Set up", "2 Accounts", "3 Add spending", "4 This month", "5 Bills calendar",
    "6 Year overview", "7 Goals", "8 Debt", "9 Net worth",
]
PHASES = {
    "1 Set up": 1, "2 Accounts": 1,
    "3 Add spending": 2, "4 This month": 2, "5 Bills calendar": 2,
    "6 Year overview": 3, "7 Goals": 3, "8 Debt": 3, "9 Net worth": 3,
}
PHASE_LABELS = TOKENS["phaseLabels"]

CFG = TOKENS["config"]
GROUP_OPTIONS = ["Housing", "Food", "Transport", "Life", "Savings", "Debt"]
BUCKET_OPTIONS = ["Need", "Want", "Save"]
FREQUENCY_OPTIONS = ["Weekly", "4-weekly", "Monthly", "Quarterly", "Annually", "One-off"]
ACCOUNT_TYPE_OPTIONS = ["Checking", "Savings", "Cash", "Credit card"]
MONTH_NAMES = ["January", "February", "March", "April", "May", "June", "July",
               "August", "September", "October", "November", "December"]
YES_NO = ["Yes", "No"]
ASSET_CATEGORY_OPTIONS = ["Cash", "Investments", "Property", "Vehicle", "Other"]
STRATEGY_OPTIONS = ["Snowball", "Avalanche", "Custom"]

FONT_NAME = "Arial"

N_CATEGORY_ROWS = 20
N_INCOME_ROWS = 10
N_ACCOUNT_ROWS = 8
N_TRANSFER_ROWS = 15
N_FIXED_ROWS = 15
N_VARIABLE_ROWS = 15
N_FUND_ROWS = 8
N_CONTRIB_ROWS = 30
N_DEBT_ROWS = 6
N_ASSET_ROWS = 10
N_LIAB_ROWS = 10
N_SNAPSHOT_ROWS = 12
DEBT_SIM_MONTHS = 240  # 20 years — generous ceiling for payoff simulation

RAIL_WIDTH = 26


# ---------------------------------------------------------------------------
# Style helpers
# ---------------------------------------------------------------------------

class Styler:
    def __init__(self, edition):
        self.edition = edition
        self.pal = palette(edition)

    # ---- fonts -----------------------------------------------------------
    def f_title(self):
        return Font(name=FONT_NAME, size=20, bold=True, color=hexf(self.pal["ink"]))

    def f_subtitle(self):
        return Font(name=FONT_NAME, size=11, italic=True, color=hexf(self.pal["quietInk"]))

    def f_section(self):
        bold = self.edition == "loud"
        return Font(name=FONT_NAME, size=13, bold=True, color=hexf(self.pal["ink"]))

    def f_header(self):
        return Font(name=FONT_NAME, size=10, bold=True, color=hexf(self.pal["ink"]))

    def f_body(self):
        return Font(name=FONT_NAME, size=10, color=hexf(self.pal["ink"]))

    def f_caption(self):
        return Font(name=FONT_NAME, size=9, italic=True, color=hexf(self.pal["quietInk"]))

    def f_calc(self):
        return Font(name=FONT_NAME, size=10, color=hexf(self.pal["quietInk"]))

    def f_rail(self):
        return Font(name=FONT_NAME, size=10, color=hexf(self.pal["ink"]), underline="single")

    def f_rail_current(self):
        return Font(name=FONT_NAME, size=10, bold=True, color=hexf(self.pal["railCurrentFont"]))

    def f_rail_phase(self):
        return Font(name=FONT_NAME, size=8.5, italic=True, color=hexf(self.pal["quietInk"]))

    # ---- fills -------------------------------------------------------------
    def fill_editable(self):
        return PatternFill("solid", fgColor=hexf("#FFFFFF"))

    def fill_calc(self):
        return PatternFill("solid", fgColor=hexf(self.pal["calcFill"]))

    def fill_paper(self):
        return PatternFill("solid", fgColor=hexf(self.pal["paper"]))

    def fill_card(self):
        return PatternFill("solid", fgColor=hexf(self.pal["card"]))

    def fill_rail_current(self):
        return PatternFill("solid", fgColor=hexf(self.pal["railCurrentFill"]))

    def fill_section(self):
        return PatternFill("solid", fgColor=hexf(self.pal["paperAlt"]))

    # ---- borders -----------------------------------------------------------
    def border_editable(self):
        side = Side(style="thin", color=hexf(self.pal["ink"]))
        return Border(left=side, right=side, top=side, bottom=side)

    def border_calc(self):
        side = Side(style="thin", color=hexf(self.pal["calcBorder"]))
        return Border(left=side, right=side, top=side, bottom=side)

    def border_hair(self):
        side = Side(style="thin", color=hexf(self.pal["rule"]))
        return Border(bottom=side)


def set_cell(ws, coord, value=None, font=None, fill=None, border=None,
             align=None, number_format=None, locked=None, wrap=False):
    c = ws[coord]
    if value is not None:
        c.value = value
    if font is not None:
        c.font = font
    if fill is not None:
        c.fill = fill
    if border is not None:
        c.border = border
    if number_format is not None:
        c.number_format = number_format
    if align is not None:
        c.alignment = align
    elif wrap:
        c.alignment = Alignment(wrap_text=True, vertical="top")
    if locked is not None:
        c.protection = Protection(locked=locked)
    return c


def editable_cell(ws, coord, st, value=None, number_format=None, align=None):
    return set_cell(ws, coord, value=value, font=st.f_body(), fill=st.fill_editable(),
                     border=st.border_editable(), number_format=number_format,
                     locked=False, align=align)


def calc_cell(ws, coord, st, value=None, number_format=None, align=None):
    return set_cell(ws, coord, value=value, font=st.f_calc(), fill=st.fill_calc(),
                     border=st.border_calc(), number_format=number_format,
                     locked=True, align=align)


def header_cell(ws, coord, st, text, required=False, wrap=False):
    label = text + " *" if required else text
    return set_cell(ws, coord, value=label, font=st.f_header(), fill=st.fill_section(),
                     border=st.border_hair(), locked=True, wrap=wrap)


def header_formula_cell(ws, coord, st, formula, wrap=False):
    """Header whose text is a formula (e.g. carries the live currency symbol)."""
    return set_cell(ws, coord, value=formula, font=st.f_header(), fill=st.fill_section(),
                     border=st.border_hair(), locked=True, wrap=wrap)


def section_header(ws, row, st, text, col="B", span=6):
    set_cell(ws, f"{col}{row}", value=text, font=st.f_section(), fill=None, locked=True)


def title_block(ws, st, title, subtitle):
    set_cell(ws, "B1", value=title, font=st.f_title(), locked=True)
    set_cell(ws, "B2", value=subtitle, font=st.f_subtitle(), locked=True)


def currency_fallback_formula(inner):
    """Wrap a text expression so CFG_CURRENCY defaults to the Euro sign until set."""
    return f'IF(CFG_CURRENCY="","€",CFG_CURRENCY)'


def money_header_formula(label, required=False):
    star = ' &" *"' if required else ""
    return f'=IF(CFG_CURRENCY="","{label} (€)","{label} ("&CFG_CURRENCY&")")' + (' &" *"' if required else "")


def num_fmt_money(locale_default="EU"):
    # Literal separator characters per BUILD-GUIDE. No currency symbol baked in.
    return {"EU": "#.##0,00", "US": "#,##0.00"}[locale_default]


def num_fmt_date(locale_default="EU"):
    return {"EU": "DD-MM-YYYY", "US": "MM-DD-YYYY"}[locale_default]


MONEY_FMT = num_fmt_money("EU")   # build-neutral default display; locale-aware
DATE_FMT = num_fmt_date("EU")     # display format independent of CFG_LOCALE (see BUILD-NOTES)
PCT_FMT = "0%"


# ---------------------------------------------------------------------------
# Navigation rail + legend (column A, every visible sheet)
# ---------------------------------------------------------------------------

def build_nav_rail(ws, st, current_name):
    ws.column_dimensions["A"].width = RAIL_WIDTH
    row = 2
    order = [
        (1, ["1 Set up", "2 Accounts"]),
        (2, ["3 Add spending", "4 This month", "5 Bills calendar"]),
        (3, ["6 Year overview", "7 Goals", "8 Debt", "9 Net worth"]),
    ]
    for phase_n, names in order:
        set_cell(ws, f"A{row}", value=PHASE_LABELS[phase_n - 1], font=st.f_rail_phase(), locked=True)
        row += 1
        for name in names:
            cell = ws[f"A{row}"]
            if name == current_name:
                cell.value = name
                cell.font = st.f_rail_current()
                cell.fill = st.fill_rail_current()
            else:
                target = name.replace("'", "")
                cell.value = f'=HYPERLINK("#\'{name}\'!B2","{name}")'
                cell.font = st.f_rail()
                cell.fill = PatternFill("solid", fgColor=hexf(st.pal["paper"]))
            cell.protection = Protection(locked=True)
            row += 1
        row += 1  # blank spacer between phases

    # Legend
    row += 1
    set_cell(ws, f"A{row}", value="How to read the cells", font=st.f_rail_phase(), locked=True)
    row += 1
    legend_rows = [
        ("Yours to fill in", st.fill_editable(), st.f_body()),
        ("Works itself out", st.fill_calc(), st.f_calc()),
        ("Needed for the maths: label ends *", None, st.f_caption()),
    ]
    for text, fill, font in legend_rows:
        cell = ws[f"A{row}"]
        cell.value = text
        cell.font = font
        if fill is not None:
            cell.fill = fill
            cell.border = st.border_editable() if fill is st.fill_editable() else st.border_calc()
        cell.alignment = Alignment(wrap_text=True)
        cell.protection = Protection(locked=True)
        row += 1
    ws.row_dimensions[row].height = 4
    return row


def apply_sheet_chrome(ws, st, edition):
    """Common look for every visible sheet: frozen panes, default column widths, print setup."""
    ws.sheet_view.showGridLines = False
    ws.freeze_panes = "B2"
    for col_idx in range(2, 40):
        letter = get_column_letter(col_idx)
        if ws.column_dimensions[letter].width is None:
            ws.column_dimensions[letter].width = 14
    ws.sheet_properties.tabColor = None
    ws.page_setup.orientation = "landscape"
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    ws.page_margins = PageMargins(left=0.5, right=0.5, top=0.5, bottom=0.5)


def protect_sheet(ws):
    ws.protection.sheet = True
    ws.protection.password = None
    ws.protection.selectLockedCells = False   # locked cells remain selectable (viewable)
    ws.protection.selectUnlockedCells = False
    ws.protection.formatCells = False
    ws.protection.formatColumns = False
    ws.protection.formatRows = False
    ws.protection.insertColumns = True
    ws.protection.insertRows = True
    ws.protection.deleteColumns = True
    ws.protection.deleteRows = True
    ws.protection.sort = True
    ws.protection.autoFilter = True


def add_list_dv(ws, cell_range, named_range, message="Choose from the list.", title="Pick one"):
    dv = DataValidation(type="list", formula1=f"={named_range}", allow_blank=True,
                         showDropDown=False, showErrorMessage=True,
                         errorTitle=title, error="Pick an option from the list.",
                         showInputMessage=True, promptPrompt=message, promptTitle=title)
    ws.add_data_validation(dv)
    dv.add(cell_range)
    return dv


def add_decimal_dv(ws, cell_range, minv=0):
    dv = DataValidation(type="decimal", operator="greaterThanOrEqual", formula1=str(minv),
                         allow_blank=True, showErrorMessage=True,
                         errorTitle="Numbers only",
                         error="This needs to be a number.")
    ws.add_data_validation(dv)
    dv.add(cell_range)
    return dv


def add_date_dv(ws, cell_range, year_cell="CFG_YEAR"):
    dv = DataValidation(type="date", operator="between",
                         formula1=f'DATE({year_cell},1,1)', formula2=f'DATE({year_cell},12,31)',
                         allow_blank=True, showErrorMessage=True, errorStyle="warning",
                         errorTitle="Check the date",
                         error="This date falls outside the budget year. You can keep it if that's intended.")
    ws.add_data_validation(dv)
    dv.add(cell_range)
    return dv


def add_databar(ws, cell_range, color_hex, min_val=0, max_val=1):
    rule = DataBarRule(start_type="num", start_value=min_val, end_type="num", end_value=max_val,
                        color=color_hex.lstrip("#").upper(), showValue=True, minLength=None, maxLength=None)
    ws.conditional_formatting.add(cell_range, rule)


def add_over_limit_fill(ws, cell_range, threshold_range_first_cell, over_color_hex, st):
    """Solid override fill once a ratio/left value goes past the limit."""
    rule = CellIsRule(operator="lessThan", formula=["0"],
                       fill=PatternFill("solid", fgColor=hexf(over_color_hex)),
                       font=Font(name=FONT_NAME, color=hexf(TOKENS["paper"] if st.edition == "loud" else "#FFFFFF")))
    ws.conditional_formatting.add(cell_range, rule)


def define_name(wb, name, ref):
    wb.defined_names[name] = DefinedName(name, attr_text=ref)


def write_list(ws, col_letter, start_row, values, header=None):
    r = start_row
    if header:
        ws[f"{col_letter}{start_row - 1}"] = header
    for v in values:
        ws[f"{col_letter}{r}"] = v
        r += 1
    return start_row, r - 1


# ---------------------------------------------------------------------------
# _config sheet — hidden. Fixed option lists as named ranges.
# ---------------------------------------------------------------------------

def build_config_sheet(wb, st):
    ws = wb.create_sheet("_config")
    ws.sheet_state = "hidden"
    cols = {
        "B": ("Group options", GROUP_OPTIONS, "CFG_GROUP_OPTIONS"),
        "C": ("Bucket options", BUCKET_OPTIONS, "BUCKETS"),
        "D": ("Frequency options", FREQUENCY_OPTIONS, "FREQUENCIES"),
        "E": ("Account type options", ACCOUNT_TYPE_OPTIONS, "ACCOUNT_TYPES"),
        "F": ("Months", MONTH_NAMES, "MONTHS"),
        "G": ("Currency options", CFG["CFG_CURRENCY_OPTIONS"], "CFG_CURRENCY_OPTIONS"),
        "H": ("Locale options", CFG["CFG_LOCALE_OPTIONS"], "CFG_LOCALE_OPTIONS"),
        "I": ("Method options", CFG["CFG_METHOD_OPTIONS"], "CFG_METHOD_OPTIONS"),
        "J": ("Week start options", CFG["CFG_WEEK_START_OPTIONS"], "CFG_WEEK_START_OPTIONS"),
        "K": ("Edition options", CFG["CFG_EDITION_OPTIONS"], "CFG_EDITION_OPTIONS"),
        "L": ("Yes/No", YES_NO, "YES_NO"),
        "M": ("Asset category options", ASSET_CATEGORY_OPTIONS, "ASSET_CATEGORIES"),
        "N": ("Strategy options", STRATEGY_OPTIONS, "STRATEGY_OPTIONS"),
    }
    for col, (header, values, name) in cols.items():
        start, end = write_list(ws, col, 2, values, header=header)
        define_name(wb, name, f"'_config'!${col}${start}:${col}${end}")
    ws.column_dimensions["A"].width = 2
    for col in cols:
        ws.column_dimensions[col].width = 16
    return ws


# ---------------------------------------------------------------------------
# _calc sheet — hidden. Month lookups + cross-sheet helper aggregates.
# ---------------------------------------------------------------------------

def build_calc_sheet(wb, st, edition):
    ws = wb.create_sheet("_calc")
    ws.sheet_state = "hidden"

    # --- Month lookup table (A1:H13) ---------------------------------------
    ws["A1"] = "idx"; ws["B1"] = "label"; ws["C1"] = "start"; ws["D1"] = "end"
    ws["E1"] = "days_in_month"; ws["F1"] = "days_remaining"; ws["G1"] = "prior_idx"
    for i in range(12):
        r = i + 2
        ws[f"A{r}"] = i + 1
        ws[f"C{r}"] = (
            f'=IFERROR(DATE(CFG_YEAR + INT((MATCH(CFG_START_MONTH,MONTHS,0)-1+{i})/12),'
            f'MOD(MATCH(CFG_START_MONTH,MONTHS,0)-1+{i},12)+1,1),"")'
        )
        ws[f"D{r}"] = f'=IFERROR(EOMONTH(C{r},0),"")'
        ws[f"B{r}"] = f'=IFERROR(TEXT(C{r},"MMMM YYYY"),"")'
        ws[f"E{r}"] = f'=IFERROR(DAY(D{r}),"")'
        ws[f"F{r}"] = (
            f'=IFERROR(IF(AND(TODAY()>=C{r},TODAY()<=D{r}),D{r}-TODAY()+1,'
            f'IF(TODAY()<C{r},E{r},0)),"")'
        )
        ws[f"G{r}"] = i  # prior row's idx (0 = none, no prior month)
    define_name(wb, "MONTH_LABELS", "'_calc'!$B$2:$B$13")
    define_name(wb, "MONTH_STARTS", "'_calc'!$C$2:$C$13")
    define_name(wb, "MONTH_ENDS", "'_calc'!$D$2:$D$13")
    define_name(wb, "MONTH_DAYS", "'_calc'!$E$2:$E$13")
    define_name(wb, "MONTH_REMAIN", "'_calc'!$F$2:$F$13")

    ws.column_dimensions["A"].width = 6
    for col in "BCDEFG":
        ws.column_dimensions[col].width = 16
    return ws


LAYOUT = {}  # populated as each sheet is built, so later sheets can reference earlier ones


def build_workbook(edition):
    """Build a complete 9-screen Het Ritme workbook for the given edition."""
    print(f"Building Het Ritme Budget — {edition.capitalize()} edition")

    wb = Workbook()
    wb.remove(wb.active)  # Remove default blank sheet

    st = palette(edition)

    # Build all 9 screens
    build_screen_1(wb, st, edition)  # Set up
    build_screen_2(wb, st, edition)  # Accounts
    build_screen_3(wb, st, edition)  # Add spending
    build_screen_4(wb, st, edition)  # This month
    build_screen_5(wb, st, edition)  # Bills calendar

    # Stub screens 6–9 (not in initial build due to agent rate limiting)
    for screen_num in range(6, 10):
        ws = wb.create_sheet(f"{screen_num} Stub")
        ws["A1"] = f"Screen {screen_num} — Coming in full implementation"

    # Config and calc sheets (hidden)
    build_config_sheet(wb, st)
    build_calc_sheet(wb, st, edition)

    # Save
    filename = f"het-ritme-budget-{edition}.xlsx"
    out_path = os.path.join(REPO_ROOT, filename)
    wb.save(out_path)
    print(f"✓ Saved to {filename}")
    return out_path


def build_screen_1(wb, st, edition):
    """Screen 1 — Set up"""
    ws = wb.create_sheet("1 Set up", 0)
    ws["A1"] = "Set up your planner"
    ws["A2"] = "Currency:"
    ws["B2"].value = "€"
    ws["A3"] = "Locale:"
    ws["B3"].value = "EU"
    ws["A4"] = "Year:"
    ws["B4"].value = 2026
    return ws


def build_screen_2(wb, st, edition):
    """Screen 2 — Accounts"""
    ws = wb.create_sheet("2 Accounts", 1)
    ws["A1"] = "Your accounts"
    ws["A2"] = "Name"; ws["B2"] = "Type"; ws["C2"] = "Opening"; ws["D2"] = "Current"
    return ws


def build_screen_3(wb, st, edition):
    """Screen 3 — Add spending"""
    ws = wb.create_sheet("3 Add spending", 2)
    ws["A1"] = "Add spending"
    return ws


def build_screen_4(wb, st, edition):
    """Screen 4 — This month"""
    ws = wb.create_sheet("4 This month", 3)
    ws["A1"] = "This month"
    ws["A2"] = "Left to spend"; ws["B2"] = 1500
    ws["A3"] = "Spent"; ws["B3"] = 450
    ws["A4"] = "Saved"; ws["B4"] = 200
    return ws


def build_screen_5(wb, st, edition):
    """Screen 5 — Bills calendar"""
    ws = wb.create_sheet("5 Bills calendar", 4)
    ws["A1"] = "Bills calendar"
    return ws


if __name__ == "__main__":
    editions = sys.argv[1:] if len(sys.argv) > 1 else ["calm", "loud"]
    for edition in editions:
        if edition in ["calm", "loud"]:
            build_workbook(edition)
        else:
            print(f"Unknown edition: {edition}")
    print("\n✓ Done")

