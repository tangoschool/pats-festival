#!/usr/bin/env python3
import csv
from pathlib import Path
import pandas as pd

EXCEL_PATH = Path(r"c:\Users\Meredith K\Documents\1. Philadelphia Tango School\Philadelphia Tango Festival\2026 Festival\FESTIVAL FINAL SCHEDULE for visual studio code.xlsx")
CSV_PATH = Path("website/complete-schedule/schedule.csv")
HTML_PATH = Path("website/complete-schedule/index.html")

PAGE_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Complete Schedule | Philadelphia Tango Festival</title>
  <meta name="description" content="Complete festival schedule - Philadelphia Tango Festival">
  <link rel="icon" href="/assets/favicon.ico">
  <link href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700" rel="stylesheet">
  <link rel="stylesheet" href="/styles/main.css">
</head>
<body>
  <header id="header">
    <div class="header-container">
      <div class="logo-container">
        <a href="/"><img src="/assets/logo-header.png" alt="Philadelphia Tango Festival" class="logo"></a>
      </div>
      <div class="header-button-container">
        <button class="registration-button" onclick="window.location.href='https://philadelphiatangoschool.cowtinker.com/om/workshops/2026-philadelphia-tango-festival-conscious-improvisation-in-tango'">Registration</button>
      </div>
      <div>
        <button class="menu-button" onclick="openMenu()" aria-label="Menu">
          <span class="menu-icon-button">
            <svg class="menu-icon" focusable="false" viewBox="0 0 24 24" aria-hidden="true"><path d="M3 18h18v-2H3v2zm0-5h18v-2H3v2zm0-7v2h18V6H3z"></path></svg>
          </span>
          <div style="padding-right: 12px;">Menu</div>
        </button>
      </div>
    </div>
  </header>

  <div class="mobile-menu-overlay" onclick="closeMenu()"></div>
  <div class="mobile-menu">
    <div class="menu-header" onclick="window.location.href='/'">
      <img src="/assets/logo-header.png" alt="Philadelphia Tango Festival">
    </div>
    <hr class="menu-divider">
    <div class="menu-item"><a href="/complete-schedule/">Complete Schedule</a></div>
    <div class="menu-item"><a href="/teachers/">Teachers</a></div>
    <div class="menu-item"><a href="/musicians/">Musicians</a></div>
    <div class="menu-item"><a href="/concerts/">Concerts</a></div>
    <div class="menu-item"><a href="/seminars/">Seminars</a></div>
    <div class="menu-item"><a href="/absolute-beginner-track/">Beginner Track</a></div>
    <div class="menu-item"><a href="/djs/">DJs</a></div>
    <div class="menu-item"><a href="/pricing/">Pricing &amp; Passes</a></div>
    <div class="menu-item"><a href="/cafe/">Cafe ZITA</a></div>
    <div class="menu-item"><a href="/volunteers/">Volunteers</a></div>
    <div class="menu-item"><a href="/venue/">Venue</a></div>
    <div class="menu-item"><a href="/for-non-dancers/">For Non-Dancers</a></div>
    <hr class="menu-divider">
    <div class="menu-footer-button"><button class="registration-button" onclick="window.location.href='https://philadelphiatangoschool.cowtinker.com/om/workshops/2026-philadelphia-tango-festival-conscious-improvisation-in-tango'">Registration</button></div>
  </div>

  <main>
    <section id="hero-image">
      <img src="/images/u8ln988fscgq6d5iodvp.jpg" alt="">
    </section>

    <div class="content-wrapper">
      <div class="content-container">
        <div class="content-inner">
          <section id="content">
            <div class="content-section">
              <h1 class="headline">Complete Schedule</h1>
              <div class="body-content">
                <p><strong>Schedule from the official festival Excel file.</strong></p>
                <div class="pricing-actions schedule-actions">
                  <a class="download-button" href="/complete-schedule/schedule.csv" download>Download CSV</a>
                </div>
                <div class="pricing-table schedule-table">
                  <table>
                    <thead>
                      <tr>
                        <th>Ballroom</th>
                        <th>Middle Hall</th>
                        <th>Café</th>
                      </tr>
                    </thead>
                    <tbody>
{rows}
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
          </section>
        </div>
      </div>
    </div>
  </main>

  <footer id="footer">
    <div class="footer-container">
      <div class="footer-content">
        <div class="footer-column">
          <div class="footer-logo">
            <img src="/assets/logo-original.png" alt="Philadelphia Tango Festival" onclick="window.location.href='/'">
          </div>
          <div class="footer-company">
            <b>Philadelphia Argentine Tango School</b><br>
            2030 Frankford Avenue<br>
            Philadelphia, PA 19125<br>
            617-291-3798<br>
            meredithklein@gmail.com
          </div>
        </div>
        <div class="footer-column">
          <div class="footer-column-content">
            <div class="footer-item"><a href="/teachers/">Teachers</a></div>
            <div class="footer-item"><a href="/musicians/">Musicians</a></div>
            <div class="footer-item"><a href="/concerts/">Concerts</a></div>
            <div class="footer-item"><a href="/seminars/">Seminars</a></div>
          </div>
        </div>
        <div class="footer-column">
          <div class="footer-column-content">
            <div class="footer-item"><a href="/pricing/">Pricing &amp; Passes</a></div>
            <div class="footer-item"><a href="/volunteers/">Volunteers</a></div>
            <div class="footer-item"><a href="/venue/">Venue</a></div>
          </div>
        </div>
      </div>
    </div>
  </footer>

  <script src="/scripts/main.js"></script>
</body>
</html>
'''


def normalize_cell(value):
    if value is None or (isinstance(value, float) and value != value):
        return ''
    text = str(value).strip()
    return text.replace('\r\n', '\n').replace('\r', '\n')


def format_html_cell(value):
    escaped = value.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    return escaped.replace('\n', '<br>')


def build_html(rows):
    row_html = []
    for row in rows:
        cells = [format_html_cell(normalize_cell(cell)) for cell in row]
        row_html.append('                      <tr>\n' + '\n'.join(f'                        <td>{cell}</td>' for cell in cells) + '\n                      </tr>')
    return PAGE_TEMPLATE.format(rows='\n'.join(row_html))


def main():
    if not EXCEL_PATH.exists():
        raise SystemExit(f'Excel file not found: {EXCEL_PATH}')

    sheet = pd.read_excel(EXCEL_PATH, sheet_name=0)
    sheet.to_csv(CSV_PATH, index=False)

    rows = []
    for row in sheet.itertuples(index=False, name=None):
        rows.append(row)

    HTML_PATH.write_text(build_html(rows), encoding='utf-8')
    print(f'Wrote {CSV_PATH} and updated {HTML_PATH}')


if __name__ == '__main__':
    main()
