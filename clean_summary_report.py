'''
    clean_summary_report.py
    by: ADG 1/3/18

    functions/script for cleaning the summary report data into a useful format

    NOTES:
    data I need:  Precinct ID, Votes Roy Moore, Votes Doug Jones, Votes
        Write in
        Best format:
        {K: {k1: v1,
             k2: v2,
             k3: v3,
             },
        }

        i.e.
        {
        "2030B" : {
            "votes_jones": 1234,
            "votes_moore": 2345,
            "votes_write_in": 456,
            },
        }
        another Note: in order to link the Precinct ID's with the ID's from the GIS
        json data, I will need to append a "B" to the precinct number

        Process:
    separate across some delimiter

    Lines which contain info I need:
    0002 PREC 1020 - TOM BRADFORD                   >>Contains " PREC "
     DOUG JONES (DEM) . . . . . . . . . 1827 81.24  >>starts with " DOUG JONES"
     ROY S. MOORE (REP) . . . . . . . . 406 18.05   >>starts with " ROY S."
     WRITE-IN. . . . . . . . . . . . 16 .71         >>starts with " WRITE-IN"
'''

def clean_summary_report(file):
    '''cleans voter summary report
        returns dict{dict{}} of precinct voter information
    '''
    with open(file) as f:
        data = f.read()

        prec_dict = {}
        reports = data.split(sep="PRECINCT REPORT SPECIAL GENERAL ELECTION")

        for r in reports[1:]:
            lines = r.split(sep="\n")

            for l in lines:
                if (l.__contains__(" PREC ")):
                    key = l[10:14] + "B"
                if (l.__contains__("DOUG JONES")):
                    jones = l[36:]
                if (l.__contains__("ROY S. MOORE")):
                    moore = l[36:]
                if (l.__contains__("WRITE-IN")):
                    write_in = l[33:]

            prec_dict[key] = {"votes_jones": int(jones.split(sep=" ")[0]),
                              "votes_moore": int(moore.split(sep=" ")[0]),
                              "votes_write_in": int(write_in.split(sep=" ")[0]),
                              }

    return(prec_dict)





