import os
import datetime

myPath = os.getcwd()
files = os.listdir(myPath)

def classify_threat(line):
    # Define threat analysis rules here
    if "ESTABLISHED" in line:
        return "Highly Malicious"
    elif "NONE" in line:
        return "Not Malicious"
    else:
        return "Malicious"

for f in files:
    if f.endswith("xyz"):
        print(f)
        fx = open(f)
        lines = fx.readlines()
        fx.close()

        data = lines[0].split(",")
        mytype = data[0]
        myname = data[1]

        print(mytype + "--" + myname)
        mynewfilename = (
            mytype
            + "-"
            + str(datetime.date.today())
            + "-"
            + myname
            + "-"
            + (f.replace("'", "-")).replace(".xyz", ".csv")
        )
        new_file = open(mynewfilename, "w")
        new_file.write("PROCESSID,STATUS,LOCALIP,LOCALPORT,REMOTEIP,REMOTEPORT,Threat Classification\n")

        for i, line in enumerate(lines):
            if i == 0:
                print(line)
            else:
                # Append the threat classification to each line
                threat_classification = classify_threat(line)
                new_file.write(f"{line.strip()},{threat_classification}\n")
                print(i, line.strip(), threat_classification)
            i = i + 1

        new_file.close()
        os.remove(f)
        print(" ")
