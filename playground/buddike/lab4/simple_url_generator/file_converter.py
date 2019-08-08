import json
import os
import glob
from random import randrange
from datetime import date


class file_processor:
    def __init__(self):
        #Get settings
        settings = self.get_settings("options\\settings.json")

        self.source_folder = settings["SourceDirectory"]
        self.destination_folder = settings["DestinationDirectory"]
        self.source_file_name_pattern = settings["SourceFileNamePattern"]
        self.destination_file_name = settings["DestinationFileName"]
        self.destination_file_name_extension = settings["DestinationFileExtension"]
        self.destination_url_touse = settings["SampleURL"]
        self.destination_url_decider = settings["UrlDeciderFieldIndex"]
        self.destination_possible_values = settings["PossibleValues"]
        self.Is_Results_Enabled = settings["IsResultsEnabled"]
        self.Email_Results_FileName = settings["EmailResultsFileName"]
        self.Email_Result_Header = settings["EmailResultHeader"]
        self.Email_Result_File_Extension = settings["EmailResultFileExtension"]

    def get_settings(self,path):
        settings_file = os.path.join(os.getcwd(),path)
        print("Reading settings from " + settings_file)

        if os.path.exists(settings_file) == 0:
            print("The file does not exist")
        else:
            json_content = json.loads(open(settings_file).read())
            print("settings read..complete")

            return json_content

    def read_file_content(self):
        source_file = os.path.join(self.source_folder,self.source_file_name_pattern)
        destination_file_path = os.path.join(self.destination_folder,os.path.join(self.destination_file_name+ date.today().strftime('%Y%m%d')+ self.destination_file_name_extension))
        destination_file = open(destination_file_path, 'w')

        files = glob.glob(source_file)
        email_result_file_header_array = self.Email_Result_Header.split(",")

        for filename in files:
            with open(filename, 'r') as f:
                for line in f:
                    str_array = line.split(",")
                    line = line.strip()

                    if str_array[self.destination_url_decider] == "" or str_array[self.destination_url_decider] == "1":
                        line = (line + ',' + str(self.destination_url_touse+str(randrange(10000000))) + '\n')
                    else:
                        line = (line + ',' + '\n')
                    destination_file.write(line)
        destination_file.close()





