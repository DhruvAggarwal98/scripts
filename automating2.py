import pandas as pd
filename = "/home/daggarwa/RedHat/pac_life/benchmarks.xlsx"
fileout = open("/home/daggarwa/scripts/out.txt","w+")
# x1_file = pd.ExcelFile(filename)
# sheet = "level"
# dfs = pd.read_excel(filename,sheet_name=sheet)
# print(dfs.head())
counter = 0
with pd.ExcelFile(filename) as xls:
    for sheet_name in xls.sheet_names:
        if sheet_name == 'Level 1 - Server':
            df = pd.read_excel(xls, sheet_name=sheet_name,usecols = "B,C,F,G")
            #print(df.iterrows())
for index,row in df.iterrows():
    if counter > 2 and counter < 20:
        fileout.write("- name: |\n")
        #print(row["recommendation #"],row["title"],row["description"],row["rationale statement"])
        control_id = row["recommendation #"]
        title = row["title"]
        desc = row["description"]
        rationale = row["rationale statement"]
        fileout.write("    Control-ID: "+control_id)
        fileout.write("\n")
        fileout.write("    Title: "+title)
        fileout.write("\n")
        fileout.write("    Description: "+desc)
        fileout.write("\n")
        fileout.write("    Rationale: "+rationale)
        fileout.write("\n")
        fileout.write("  module:")
        fileout.write("\n\n")

    counter+=1
