# Important!

Please note that you can download a [flat .zip file with USDOT information directly](https://ai.fmcsa.dot.gov/SMS/Tools/Downloads.aspx) which may negate your need for hitting the FMCSA Web Service for information, as well as the need to use anything in this repo!

Though, it should be pointed out that the `.zip` file does not contain the same breadth of information available through the FMCSA API.

# DOT FMCSA SAFER Dataset

The United States DOT (Department of Transportation) provides an [API](https://safer.fmcsa.dot.gov/CompanySnapshot.aspx) for querying the FMCSA (Federal Motor Carrier Safety Administration) SAFER (Safety and Fitness Electronic Records) System.

This dataset can be used to query for the "Company Snapshot" of a company by a single US DOT (USDOT) number at a time. This allows a user to query the dataset for information on the company who owns and operates a commercial trucking vehicle in the United States.

This repo provides a script that can be used to query this dataset.

This repo does not represent an all-inclusive client. This is meant as a starting point for anyone who wants to develop a solution using this public data.

**For a full fledged client, see the [python-safer](https://github.com/arthurtyukayev/python-safer) project)**

# Run

If you have the HTML of a query result from the FMCSA SAFER dataset, you can process that HTML directly.

```
./dot.py --parse /path/to/1234567890.html
```

You can just as easily query the FMCSA SAFER dataset directly by USDOT number.

```
$ ./dot.py --query 1234567890
LegalName SOME COMPANY NAME
DBAName
PhysicalAddress 1122 BOOGIE WOOGIE AVENUE, IL 60640
Phone (555) 555-555
MailingAddress 1122 BOOGIE WOOGIE AVENUE, IL 60640
DOTNumber 1234567890
StateId 123
MCMXFF MC-123
DUNS MC-123
```

# Is The SAFER System Data Public/Free?

Yes! The [data.gov](https://catalog.data.gov/dataset?q=organization:dot-gov+AND+type:dataset&publisher=Federal+Motor+Carrier+Safety+Administration) catalog for the DOT lists the [SAFER - Company Snapshot](https://catalog.data.gov/dataset/safer-company-snapshot-safer-company-snapshot-74afd) as a free public dataset.

> Public: This dataset is intended for public access and use.

> The Company Snapshot is a concise electronic record of company identification, size, commodity information, and safety record, including the safety rating (if any), a roadside out-of-service inspection summary, and crash information. The Company Snapshot is available via an ad-hoc query (one carrier at a time) free of charge.

The interface to this data may be clunky, but the intention is clear. This is public data available for ad-hoc querying.

![screenshot](/docs/screenshot.png)

The same information regarding usage is also available directly on the [SAFER website](https://safer.fmcsa.dot.gov/about.aspx).

> The Safety and Fitness Electronic Records (SAFER) System offers company safety data to industry and the public over the internet. Access is provided free of charge to the Company Snapshot, a concise electronic record of a company’s identification, size, commodity information, and safety record, including the safety rating (if any), a roadside out-of-service inspection summary, and crash information. The company snapshot is available via an ad-hoc query (one carrier at a time).

Although this Web Service/HTML API is clunky, the fact that it is part of the open data catalog on DATA.GOV and explicitly says it is available to the public over the Internet makes it clear that this data should be safe for individuals in the public domain to query and analyze as needed. Despite extensive searching, I have not found any Terms of Service for this data regarding scraping and best practices for reading the data through this API. I've reached out to the IT department at FMCSA to see if there are better ways of accessing this data in bulk. In the meantime, any scraping done by this service is purposefully throttled to respect the resources of the DOT. 

# Development

Work on this locally however you'd prefer. One option is as follows.

```
virtualenv venv
. ./venv/bin/activate
pip install -r requirements.txt
```

And update requirements in the venv with `pip freeze > requirements.txt`

