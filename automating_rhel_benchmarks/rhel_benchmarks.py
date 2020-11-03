import pandas as pd
filename = "/home/daggarwa/scripts/automating_rhel_benchmarks/benchmarks.xlsx"
fileout = open("/home/daggarwa/scripts/automating_rhel_benchmarks/output.txt","w+")
counter = 0
with pd.ExcelFile(filename) as xls:
    for sheet_name in xls.sheet_names:
        if sheet_name == 'Level 1 - Server':
            df = pd.read_excel(xls, sheet_name=sheet_name,usecols = "B,C,F,G")
fileout.write("---")
fileout.write("\n")
for index,row in df.iterrows():
    if counter > 2:
        control_id = row["recommendation #"]
        if type(control_id) == str:
            fileout.write("- name: |\n")
            title = row["title"]
            desc = row["description"].replace("\n"," ")
            rationale = row["rationale statement"].replace("\n"," ")
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
        else:
            pass
        
    counter+=1
fileout.write("...")