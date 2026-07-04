# Data Source Decision Log

## Attempt 1: Dataful UPI PSP dataset
Paid — gated behind Dataful's subscription. Not usable for a free portfolio project.

## Attempt 2: India Data Portal "Product Wise Declined" dataset
Free, but mislabeled — actually contains NFS and AEPS data only, no UPI rows.

## Attempt 3: Scrape NPCI's live UPI Ecosystem Statistics page
NPCI's robots.txt disallows automated access to this page. Respected this 
and did not build a scraper against it.

## Attempt 4: Wayback Machine historical snapshots
Technically legitimate (different domain, not blocked by NPCI's robots.txt), 
but archive.org itself is unreachable on my network (confirmed at browser 
level, not just in Python) — likely an ISP-level block/throttle common in 
India. Confirmed this is a network constraint, not a code bug.

## Final decision
Proceeding with the NFS/AEPS dataset from India Data Portal (free, real, 
already downloaded). Reframing the project as "NPCI Digital Payments 
Failure Analysis" covering ATM network (NFS) and Aadhaar-enabled payments 
(AEPS) failure patterns instead of UPI specifically.