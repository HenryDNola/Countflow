# The words on the two legal pages.
#
# The DESIGN is Webstudio's and stays exactly as it is — this only rewrites the
# text inside the page's own paragraph, keeping its markup (a bold heading, the
# text, a line break). Edit the text below and run:
#
#     python legal-words.py
#
# NOTE: re-publishing the site from Webstudio overwrites these two files with
# whatever text is in Webstudio. Paste the same words in there, or run this
# again afterwards.
import re
import pathlib

UPDATED = '19 September 2026'

PRIVACY = [
    ('What CountFlow is',
     'CountFlow ("the App") is an app for counting retail stock, at app.countflow.dev. A store '
     'signs up, adds its people and its bays, and the App hands out bays to count and keeps the '
     'record of what was counted and by whom. This policy explains what the App collects, why, and '
     'what you can do about it.'),
    ('What we collect',
     'Your account: an email address and a password, which is stored scrambled (hashed) by our '
     'sign-in provider and cannot be read by anyone at CountFlow. Your profile: your name as your '
     'manager enters it, your role, and optionally an email address, a photo, and a four-digit PIN '
     'for shared store devices — PINs are stored scrambled too, so they can be reset but never '
     'read. Your work: the bays you are assigned and count, times, flags you raise, notes, '
     'training results, the zones you cover, the store\'s floor plans and the daily log. A few '
     'preferences stay on your own device, such as light or dark mode and which store you are '
     'looking at. When something breaks, an automatic error report is sent to our monitoring '
     'service carrying which store and which screen, never who you are, with IP address storage '
     'switched off. Our sign-in page uses Cloudflare Turnstile to keep automated sign-ups out. We '
     'do not collect location, contacts, advertising identifiers, or any third-party analytics or '
     'tracking cookies.'),
    ('Why we collect it',
     'To run the service you or your employer signed up for: to sign you in, show you your work, '
     'keep your store\'s counting records, tell your manager what needs attention, keep the service '
     'secure, and fix it when it breaks. Nothing else.'),
    ('Who can see it',
     'Managers and admins at your store can see that store\'s roster, counting records and reports '
     '— that is the purpose of the App. Every store is walled off from every other store, enforced '
     'by the database itself rather than by the screens. We may access a store\'s data to support '
     'or repair the service, and where the law requires it, but we do not browse it otherwise. We '
     'never sell, rent or share your information with advertisers or data brokers.'),
    ('Who processes it for us',
     'Supabase (database, sign-in and file storage, United States); Vercel (hosting the App); '
     'Cloudflare (bot protection on the sign-in page); Sentry (error reports, United States); '
     'GitHub (encrypted weekly backups). They process data on our behalf and may not use it for '
     'their own purposes.'),
    ('Photos',
     'A profile photo is optional, and a store\'s manager can switch photos off for the whole '
     'store. A photo is stored at an address made of two random identifiers: anyone holding that '
     'exact address can view the image, which is what keeps the App fast and free, but nobody can '
     'browse or list the photos. You can remove your photo at any time, and your manager can '
     'remove it for you.'),
    ('How long we keep it',
     'Counting records are kept while the store is active, because they are the store\'s own '
     'history. Backups are kept for 90 days and then deleted, as are error reports. If a store '
     'closes its account we delete its data within 30 days, except anything the law requires us to '
     'keep.'),
    ('Your choices and rights',
     'You can ask us for a copy of your information, to correct something wrong, to delete your '
     'account and personal information, or to stop processing it where the law gives you that '
     'right. Write to privacy@countflow.dev and we will answer within 30 days. Some information '
     'has to stay: your store\'s counting records belong to the store, and removing your name from '
     'them would falsify the store\'s own history, so we disconnect them from you rather than '
     'rewrite them. Depending on where you live you may have specific rights under laws such as '
     'the GDPR or the CCPA; we apply the same standards to everyone.'),
    ('Security',
     'Sign-in is handled by a specialist provider, passwords and PINs are stored scrambled, and '
     'everything travels encrypted. No part of the App writes to the database directly: every '
     'change goes through a checked, server-side rule, each store\'s data is isolated at the '
     'database level, and administrative actions are written to an audit log. No system is '
     'perfect; if a breach ever affects your information we will tell you and the relevant '
     'regulator promptly.'),
    ('Children',
     'CountFlow is a workplace tool and is not intended for children under 13. We do not knowingly '
     'collect their information. If you believe a child has an account, write to us and we will '
     'remove it.'),
    ('Changes',
     'If this policy changes in a way that matters, we will say so in the App before it takes '
     'effect, and the date above will change.'),
    ('Contact',
     'Questions about this policy, or a request about your information: privacy@countflow.dev.'),
]

TERMS = [
    ('What these terms are',
     'These terms are the agreement between you and CountFlow for use of the CountFlow app at '
     'app.countflow.dev. Creating an account means you agree to them. If you do not, please do not '
     'create one.'),
    ('What CountFlow is',
     'An app for counting retail stock: it hands out bays to count, records what was counted and by '
     'whom, and reports on it. We provide the tool; what your store does with it is your store\'s '
     'business.'),
    ('Accounts',
     'Your account is yours alone, so do not share your password. You must be old enough to work '
     'where you live, and at least 13. Keep your email address current, because it is how you '
     'recover your account, and tell us promptly if you think someone else has got into it.'),
    ('Stores, and who is in charge of one',
     'Whoever creates a store owns it and decides who else is in it and what they can do. A '
     'store\'s data belongs to the store, not to us and not to whoever typed it in; if you are an '
     'employee, your manager can see the work you do in the app, which is what it is for. The '
     'owner is responsible for having the right to enter the information they enter, including '
     'employees\' names and email addresses, and for telling their people that the store uses '
     'CountFlow. If an owner asks us to delete a store, we delete it and everything in it.'),
    ('Paying for it',
     'A new store starts with a free trial; after that, paid features require a subscription. '
     'Prices and what is included are shown before you pay, and if they change we will tell you '
     'before the change applies to you. Subscriptions renew until cancelled — cancel any time and '
     'keep it until the period you have paid for ends. Fees are exclusive of tax unless stated.'),
    ('Using it properly',
     'Do not break the law with it, try to get into someone else\'s store or account, probe or '
     'attack the service, scrape it, resell it as your own, upload anything you have no right to '
     'upload, or use it to harass anyone. We can suspend an account or a store doing those things, '
     'and we will say why.'),
    ('Your content',
     'You keep ownership of what you put in — names, notes, floor plans, photos. You give us '
     'permission to store and display it as needed to run the service for you, and nothing else. '
     'We do not use your content to advertise and we do not sell it. Photos are optional, and a '
     'store can turn them off entirely.'),
    ('Availability',
     'We work to keep the service up and we back it up, but this is software: it can be down and it '
     'can have faults. We do not promise uninterrupted or error-free service. We may change or '
     'remove features, and if we remove something you depend on we will give reasonable notice.'),
    ('Your records',
     'You can export your store\'s data at any time. If we ever shut the service down, we will give '
     'at least 30 days\' notice and a way to take your data with you.'),
    ('Warranties and liability',
     'The service is provided "as is", without warranties beyond those the law requires and will '
     'not let us exclude. To the extent the law allows, we are not liable for lost profits, lost '
     'data, or indirect or consequential losses, and our total liability for any claim is limited '
     'to what you paid us in the twelve months before it arose. Nothing here limits liability for '
     'death or personal injury caused by negligence, for fraud, or for anything else the law says '
     'cannot be limited.'),
    ('Ending it',
     'You can stop using CountFlow and delete your account whenever you like. We can end your '
     'access if you break these terms, do not pay, or use the service in a way that risks harm to '
     'others — with notice, unless the risk means we have to act immediately.'),
    ('Changes to these terms',
     'If we change them in a way that matters, we will tell you in the app before the change takes '
     'effect, and the date above will change. Carrying on using CountFlow after that means you '
     'accept the new version.'),
    ('Law',
     'These terms are governed by the law of the United States and of the state in which CountFlow '
     'is operated, and disputes belong to the courts there.'),
    ('Contact',
     'Questions about these terms: support@countflow.dev.'),
]


def esc(s):
    return (s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
             .replace('"', '&quot;').replace("'", '&#x27;'))


def body(sections):
    out = [f'<b class="w-element">Last updated {esc(UPDATED)}</b><br/>']
    for i, (title, text) in enumerate(sections, 1):
        out.append(f'<b class="w-element">{i}. {esc(title)}</b> {esc(text)}<br/>')
    return ''.join(out)


# Every page's "GET COUNTFLOW" button points at the app. (It used to open a
# Google Sheets template — the product hasn't been that for months.)
OLD_BUTTON = 'https://docs.google.com/spreadsheets/d/1K8tJkBP1QB2iLmN9M-AG_zc5sUXFjGqNvtH6yi6tLrI/template/preview'
APP = 'https://app.countflow.dev'

root = pathlib.Path(__file__).resolve().parent
for page in list(root.glob('*.html')) + list(root.glob('*/index.html')):
    t = page.read_text(encoding='utf-8')
    if OLD_BUTTON in t:
        page.write_text(t.replace(OLD_BUTTON, APP), encoding='utf-8')
        print('pointed the Get CountFlow button at the app on', page.name)

for folder, sections in [('privacy-policy', PRIVACY), ('terms-of-service', TERMS)]:
    f = root / folder / 'index.html'
    html = f.read_text(encoding='utf-8')
    pat = re.compile(r'(<p class="w-element c13madgv[^"]*">)(.*?)(</p>)', re.S)
    found = pat.search(html)
    if not found:
        raise SystemExit(f'{folder}: could not find the text block — page markup changed?')
    html = pat.sub(lambda m: m.group(1) + body(sections) + m.group(3), html, count=1)
    f.write_text(html, encoding='utf-8')
    print('rewrote the words in', folder + '/index.html')
