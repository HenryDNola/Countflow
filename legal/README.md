# The legal pages

`privacy-policy/index.html` and `terms-of-service/index.html` are **not**
Webstudio's export any more. They are generated from `legal/build.py`, which
holds the actual words, so they can be updated the same way the app is:
edit, commit, push, live.

    python legal/build.py

Why: both pages have to say exactly what the app does, they change when the app
changes, and the app links to them from its sign-up screen.

**If the site is re-published from Webstudio**, its export will overwrite these
two files with the old versions. Run the build again and push.
