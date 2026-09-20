# Builds countflow.dev's two legal pages from the text below.
#
# Why these two pages are hand-written instead of Webstudio's export: they have
# to say exactly what the app does, they change when the app changes, and we
# want to update them the way we update everything else — edit, commit, push,
# live. Run:  python legal/build.py
#
# NOTE: re-publishing the site from Webstudio will overwrite these two files.
# If that happens, run this again.
import html
import pathlib

UPDATED = '19 September 2026'
CONTACT = 'support@countflow.dev'
PRIVACY_CONTACT = 'privacy@countflow.dev'

SHELL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · CountFlow</title>
<meta name="description" content="{title} for CountFlow, the app for counting retail stock.">
<link rel="icon" href="/icon-192.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<style>
  :root {{
    --bg: #0E1418; --card: #151D22; --edge: #24313A;
    --ink: #E8EEF1; --ink-2: #A9BAC4; --ink-3: #7D8E99; --teal: #22A6A0;
  }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0; padding: 0 20px 72px; background: var(--bg); color: var(--ink);
    font: 400 16px/1.65 system-ui, -apple-system, 'Segoe UI', sans-serif;
  }}
  .wrap {{ max-width: 760px; margin: 0 auto; }}
  header {{ padding: 40px 0 26px; text-align: center; }}
  .logo {{ width: 76px; height: 76px; border-radius: 18px; }}
  .word {{ font: 800 26px/1 system-ui; letter-spacing: .07em; margin-top: 14px; }}
  .word span {{ color: var(--teal); }}
  h1 {{ font-size: 30px; line-height: 1.2; margin: 26px 0 6px; }}
  .updated {{ color: var(--ink-3); font-size: 13px; margin: 0 0 26px; }}
  .lede {{ color: var(--ink-2); font-size: 17px; }}
  section {{
    background: var(--card); border: 1px solid var(--edge); border-top: 2px solid var(--teal);
    border-radius: 14px; padding: 20px 22px; margin: 16px 0;
  }}
  h2 {{ font-size: 17px; margin: 0 0 8px; }}
  p, li {{ color: var(--ink-2); }}
  p {{ margin: 0 0 10px; }}
  ul {{ margin: 0 0 10px; padding-left: 20px; }}
  li {{ margin: 5px 0; }}
  strong {{ color: var(--ink); }}
  a {{ color: var(--teal); }}
  table {{ width: 100%; border-collapse: collapse; margin: 6px 0 10px; }}
  th, td {{ text-align: left; padding: 8px 10px; border-bottom: 1px solid var(--edge); font-size: 14px; }}
  th {{ color: var(--ink-3); font: 700 11px/1 system-ui; letter-spacing: .08em; text-transform: uppercase; }}
  nav {{ text-align: center; padding: 26px 0 0; border-top: 1px solid var(--edge); margin-top: 30px; }}
  nav a {{ margin: 0 10px; font-size: 14px; }}
  @media (max-width: 560px) {{ h1 {{ font-size: 25px; }} section {{ padding: 16px; }} }}
</style>
</head>
<body>
<div class="wrap">
  <header>
    <img class="logo" src="/icon-192.png" alt="CountFlow">
    <div class="word">COUNT<span>FLOW</span></div>
  </header>
  <h1>{title}</h1>
  <p class="updated">Last updated {updated}</p>
  {body}
  <nav>
    <a href="/">Home</a><a href="/privacy-policy/">Privacy Policy</a><a href="/terms-of-service/">Terms of Service</a>
  </nav>
</div>
</body>
</html>
"""


def section(title, *blocks):
    inner = ''.join(blocks)
    return f'<section><h2>{html.escape(title)}</h2>{inner}</section>\n  '


def p(text):
    return f'<p>{text}</p>'


def ul(*items):
    return '<ul>' + ''.join(f'<li>{i}</li>' for i in items) + '</ul>'


PRIVACY = [
    p('<span class="lede">CountFlow is an app for counting retail stock. This policy explains what '
      'it collects, why, and what you can do about it. Questions or requests: '
      f'<a href="mailto:{PRIVACY_CONTACT}">{PRIVACY_CONTACT}</a>.</span>'),
    section('The short version',
            ul('We collect what the app needs to do its job: who you are, what store you are in, '
               'and the counting work you do there.',
               'We do not sell anything about you, we do not advertise, and we do not track you '
               'across other websites.',
               "Your store's data belongs to your store. Other stores cannot see it.",
               'You can ask for a copy of your information, or ask us to delete it.')),
    section('What we collect',
            p('<strong>Your account.</strong> Your email address and a password. Passwords are '
              'stored scrambled (hashed) by our sign-in provider; nobody at CountFlow can read them.'),
            p('<strong>Your profile.</strong> Your name as your manager enters it, your job role, '
              'and optionally an email address, a photo, and a four-digit PIN for shared store '
              'devices. PINs are stored scrambled too: they can be reset, never read.'),
            p('<strong>Your work.</strong> The bays you are assigned and count, times, flags you '
              'raise, notes, training quiz results, the zones you cover, the store\'s floor plans '
              'and the daily log. This is the record the app exists to keep, and your manager can '
              'see it.'),
            p('<strong>Your device, in small amounts.</strong> A few preferences stay on the device '
              'itself — light or dark mode, your store\'s colours, which store you are looking at, '
              'which notices you have dismissed.'),
            p('<strong>Error reports.</strong> When something breaks, an automatic report goes to '
              'our error-monitoring service so we can fix it. Those reports carry which store and '
              'which screen, never who you are, and we have turned off IP address storage there.'),
            p('<strong>Bot protection.</strong> Our sign-in page uses Cloudflare Turnstile to keep '
              'automated sign-ups out. Cloudflare receives what it needs to run that check.'),
            p('<strong>What we do not collect.</strong> No location tracking, no contacts, no '
              'microphone or camera access beyond a photo you choose to upload, no advertising '
              'identifiers, and no third-party analytics or tracking cookies of any kind.')),
    section('Why we collect it',
            p('To run the service you or your employer signed up for: to sign you in, show you your '
              'work, keep your store\'s counting records, tell your manager what needs attention, '
              'keep the service secure, and fix it when it breaks. Nothing else.')),
    section('Who can see it',
            ul('<strong>Your store.</strong> Managers and admins at your store see the roster, the '
               'counting records and the reports for that store. That is the point of the app.',
               '<strong>Other stores cannot.</strong> Every store is walled off from every other, '
               'enforced by the database itself rather than by the screens.',
               '<strong>Us.</strong> We may access a store\'s data to support or repair the service, '
               'and where the law requires it. We do not browse it otherwise.',
               '<strong>Our service providers</strong>, listed below, who process data on our behalf '
               'and may not use it for their own purposes.',
               '<strong>Nobody else.</strong> We do not sell, rent or share your information with '
               'advertisers or data brokers.')),
    section('Who processes it for us',
            '<table><tr><th>Provider</th><th>What they do</th><th>Where</th></tr>'
            '<tr><td>Supabase</td><td>Database, sign-in, file storage</td><td>United States</td></tr>'
            '<tr><td>Vercel</td><td>Hosting and delivery of the app</td><td>United States / global</td></tr>'
            '<tr><td>Cloudflare</td><td>Bot protection on sign-in</td><td>Global</td></tr>'
            '<tr><td>Sentry</td><td>Error reports</td><td>United States</td></tr>'
            '<tr><td>GitHub</td><td>Encrypted weekly backups</td><td>United States</td></tr></table>'),
    section('Photos',
            p('A profile photo is optional, and a store\'s manager can switch photos off for the '
              'whole store. A photo is stored at an address made of two random identifiers: anyone '
              'holding that exact address can view the image, which is what keeps the app fast and '
              'free, but nobody can browse or list the photos. You can remove your photo at any '
              'time, and your manager can remove it for you.')),
    section('How long we keep it',
            ul('Counting records are kept while the store is active — they are the store\'s own history.',
               'Backups are kept for 90 days, then deleted.',
               'If a store closes its account, we delete its data within 30 days, except where the '
               'law requires us to keep something.',
               'Error reports are kept for 90 days.')),
    section('Your choices and rights',
            p('You can ask us to give you a copy of your information, correct something wrong, '
              'delete your account and personal information, or stop processing it where the law '
              f'gives you that right. Write to <a href="mailto:{PRIVACY_CONTACT}">{PRIVACY_CONTACT}</a> '
              'and we will answer within 30 days.'),
            p('Some information has to stay: your store\'s counting records belong to the store, and '
              'removing your name from them would falsify the store\'s own history — so we '
              'disconnect them from you rather than rewrite them.'),
            p('Depending on where you live you may have specific rights under laws such as the GDPR '
              'or the CCPA. We apply the same standards to everyone.')),
    section('Security',
            p('Sign-in is handled by a specialist provider, passwords and PINs are stored scrambled, '
              'and everything travels encrypted. No part of the app writes to the database directly: '
              'every change goes through a checked, server-side rule, and each store\'s data is '
              'isolated at the database level. Administrative actions are written to an audit log. '
              'No system is perfect; if a breach ever affects your information we will tell you and '
              'the relevant regulator promptly.')),
    section('Children',
            p('CountFlow is a workplace tool and is not intended for children under 13. We do not '
              'knowingly collect their information. If you believe a child has an account, write to '
              'us and we will remove it.')),
    section('Changes',
            p('If this policy changes in a way that matters, we will say so in the app before it '
              'takes effect, and the date at the top will change.')),
    section('Contact',
            p(f'CountFlow — <a href="mailto:{PRIVACY_CONTACT}">{PRIVACY_CONTACT}</a> — countflow.dev')),
]

TERMS = [
    p('<span class="lede">These terms are the agreement between you and CountFlow for use of the '
      'app at app.countflow.dev. Creating an account means agreeing to them.</span>'),
    section('1. What CountFlow is',
            p('An app for counting retail stock: it hands out bays to count, records what was '
              'counted and by whom, and reports on it. We provide the tool. What your store does '
              'with it is your store\'s business.')),
    section('2. Accounts',
            ul('Your account is yours alone. Do not share your password.',
               'You must be old enough to work where you live, and at least 13.',
               'Keep your email address current — it is how you recover your account.',
               'Tell us promptly if you think someone else has got into your account.')),
    section('3. Stores, and who is in charge of one',
            ul('Whoever creates a store owns it, and decides who else is in it and what they can do.',
               '<strong>A store\'s data belongs to the store</strong>, not to us and not to whoever '
               'typed it in. If you are an employee, your manager can see the work you do in the '
               'app; that is what it is for.',
               'The owner is responsible for having the right to enter the information they enter, '
               'including employees\' names and email addresses, and for telling their people that '
               'the store uses CountFlow.',
               'If an owner asks us to delete a store, we delete it and everything in it.')),
    section('4. Paying for it',
            ul('A new store starts with a free trial. After that, paid features need a subscription.',
               'Prices and what is included are shown before you pay. If they change, we will tell '
               'you before the change applies to you.',
               'Subscriptions renew until cancelled. Cancel any time and keep it until the period '
               'you have paid for ends.',
               'Fees are exclusive of tax unless stated.')),
    section('5. Using it properly',
            p('Do not break the law with it, try to get into someone else\'s store or account, probe '
              'or attack the service, scrape it, resell it as your own, upload anything you have no '
              'right to upload, or use it to harass anyone. We can suspend an account or a store '
              'doing those things, and we will say why.')),
    section('6. Your content',
            p('You keep ownership of what you put in — names, notes, floor plans, photos. You give '
              'us permission to store and display it as needed to run the service for you, and '
              'nothing else. We do not use your content to advertise and we do not sell it. Photos '
              'are optional and a store can turn them off entirely.')),
    section('7. Availability',
            p('We work to keep it up and we back it up, but this is software: it can be down, and it '
              'can have faults. We do not promise uninterrupted or error-free service. We may change '
              'or remove features; if we remove something you depend on, we will give reasonable '
              'notice.')),
    section('8. Your records',
            p('You can export your store\'s data at any time. If we ever shut the service down, we '
              'will give at least 30 days\' notice and a way to take your data with you.')),
    section('9. Warranties and liability',
            p('The service is provided "as is", without warranties beyond those the law requires and '
              'will not let us exclude. To the extent the law allows, we are not liable for lost '
              'profits, lost data, or indirect or consequential losses, and our total liability for '
              'any claim is limited to what you paid us in the twelve months before it arose.'),
            p('Nothing here limits liability for death or personal injury caused by negligence, for '
              'fraud, or for anything else the law says cannot be limited.')),
    section('10. Ending it',
            p('You can stop using CountFlow and delete your account whenever you like. We can end '
              'your access if you break these terms, do not pay, or use the service in a way that '
              'risks harm to others — with notice, unless the risk means we have to act immediately.')),
    section('11. Changes to these terms',
            p('If we change them in a way that matters, we will tell you in the app before the '
              'change takes effect, and the date at the top will change. Carrying on using CountFlow '
              'after that means accepting the new version.')),
    section('12. Law',
            p('These terms are governed by the law of the United States and of the state in which '
              'CountFlow is operated, and disputes belong to the courts there.')),
    section('13. Contact',
            p(f'CountFlow — <a href="mailto:{CONTACT}">{CONTACT}</a> — countflow.dev')),
]

root = pathlib.Path(__file__).resolve().parent.parent
for folder, title, blocks in [('privacy-policy', 'Privacy Policy', PRIVACY),
                              ('terms-of-service', 'Terms of Service', TERMS)]:
    page = SHELL.format(title=title, updated=UPDATED, body=''.join(blocks))
    (root / folder / 'index.html').write_text(page, encoding='utf-8')
    print('wrote', folder + '/index.html', len(page), 'bytes')
