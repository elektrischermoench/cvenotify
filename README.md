# cvenotify

cvenotify is a very simple python3 script, which can be used to setup automated notifications of cve entries.
It is using the web API of https://github.com/cve-search/cve-search

It is using a simple MongoDB with the following format (JSON):

```
[{"version": "1.0.1b", "lastcve": "CVE-0000-0000", "vendor": "openssl", "product": "openssl"},
{"version": "1.0.1f", "lastcve": "CVE-0000-0000", "vendor": "openssl", "product": "openssl"},
{"version": "1.0.3", "lastcve": "CVE-0000-0000", "vendor": "openssl", "product": "openssl"},
{"version": "1.0.1d", "lastcve": "CVE-0000-0000", "vendor": "openssl", "product": "openssl"}]
```
For setup of cvenotify just run
```
python3 createdb.py
```

To start cvenotifiy just use
```
python3 cvenotify.py
```

cvenotify sends simple mails with an link to new foud cve-entries. Set up a cronjob e.g. to be up-to-date about new 
vulnerabilities to your used products.
