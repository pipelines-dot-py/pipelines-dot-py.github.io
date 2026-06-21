# Connecting pipelinesdotpy.com to Your GitHub Pages Site

This walks through registering the domain and pointing it at your existing
`pipelines-dot-py.github.io` site. Your site keeps working at the old URL
throughout this process — nothing breaks while you set this up.

---

## Step 1 — Register the domain

1. On Namecheap, search for `pipelinesdotpy.com` and add it to cart
2. You're registering for **2 years** — confirm that term at checkout
3. **Keep "WhoisGuard" (free privacy protection) enabled** — Namecheap
   includes this at no cost for `.com` domains. It hides your personal
   contact info from public WHOIS lookups. Don't pay extra for any
   "premium" version if offered
4. **Decline upsells** for things you don't need: SSL certificates (GitHub
   Pages provides this free, covered in Step 5), email hosting, website
   builder, premium DNS — none of it is necessary for this setup
5. Complete checkout

That's the only purchase required. Hosting (GitHub Pages), SSL, and basic
DNS management are all free and already covered by what you have.

---

## Step 2 — Add the domain in GitHub Pages settings (do this first)

GitHub recommends doing this *before* touching DNS, so the domain is
already expected on their end when traffic starts arriving.

1. Go to your repo → **Settings → Pages**
2. Under **Custom domain**, type `pipelinesdotpy.com` → click **Save**
3. GitHub will automatically commit a `CNAME` file to your repo root
   containing that domain — you don't need to create this yourself
4. It'll show as unverified/pending until DNS is configured — that's expected

---

## Step 3 — Configure DNS in Namecheap

1. In Namecheap, go to **Domain List** → click **Manage** next to
   `pipelinesdotpy.com` → **Advanced DNS** tab
2. Remove any default "Parking Page" records Namecheap auto-creates
3. Add these records:

**Four A records** (point the apex domain to GitHub's servers):

| Type | Host | Value |
|---|---|---|
| A Record | @ | 185.199.108.153 |
| A Record | @ | 185.199.109.153 |
| A Record | @ | 185.199.110.153 |
| A Record | @ | 185.199.111.153 |

**One CNAME record** (so `www.pipelinesdotpy.com` also works):

| Type | Host | Value |
|---|---|---|
| CNAME Record | www | pipelines-dot-py.github.io |

Leave TTL at the default ("Automatic") for all of them.

---

## Step 4 — Wait for propagation

DNS changes can take anywhere from a few minutes to 24 hours to fully
propagate. Check status by visiting `https://pipelinesdotpy.com` directly,
or using Windows PowerShell:

```
Resolve-DnsName pipelinesdotpy.com
```

You're looking for it to return the four GitHub IP addresses from Step 3.

---

## Step 5 — Enable HTTPS

Once DNS resolves correctly, go back to **Settings → Pages** on GitHub.
You should see a checkbox for **Enforce HTTPS** become available (it's
greyed out until GitHub finishes issuing a free certificate for your
domain, which can take anywhere from a few minutes to a few hours after
DNS propagates). Check it once available. This is the free SSL certificate
mentioned in Step 1 — no separate purchase needed.

---

## Step 6 — Push the updated site files

I've already updated the canonical URLs, sitemap, and robots.txt in your
site files to point to `pipelinesdotpy.com` instead of the old GitHub URL.
Download the updated files, overwrite them in your repo, then:

```
git add .
git commit -m "Switch canonical domain to pipelinesdotpy.com"
git push
```

---

## Step 7 — Update your social media bios

Once `https://pipelinesdotpy.com` is confirmed live, swap it into:
- Instagram bio link
- TikTok bio link
- YouTube channel link

---

## Step 8 — Set a renewal reminder

You registered for 2 years, so this is easy to forget. Namecheap will
email renewal reminders, but it's worth also adding a personal reminder a
month or two before expiration so the domain doesn't lapse unexpectedly.
You can also enable auto-renew in Namecheap (requires a payment method on
file) if you'd rather not think about it at all.

---

## Note on the old URL

`pipelines-dot-py.github.io` will keep working — GitHub doesn't disable it.
Anyone who already has that link bookmarked or shared won't hit a dead end.
`pipelinesdotpy.com` just becomes the one you actively promote going forward.
