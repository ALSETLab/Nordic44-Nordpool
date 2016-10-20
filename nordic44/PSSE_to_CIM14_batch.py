# This script is designed to be run from ODMS (Tools->Run Python Script)
import os
import glob

# (Adjust local directory paths as needed)
dir_list = glob.glob("G:\WP7_iTesla\BC_N44\Py_N44\N44_*/") # List all directories with PSSE raw files
for w in range (0,len(dir_list)):
  os.chdir(str(dir_list[w])) #set the working directory as the one with the Nord Pool Excel files
  output_dir = 'CIM14'
  
  map_file = 'N44_RDFIDMAP.xml'
  raw_prefix = 'h'
  model_prefix = 'N44_h'

  # Create and intialize an ImportExportOptions object
  options = odmsPy.ImportExportOptions()
  options.PSSEversion = 33
  options.CIMversion = odmsPy.CIMversion.CIM14

  # (Adjust local database options as needed)
  options.DBtype = odmsPy.DatabaseType.SQLServer
  options.Server = r'.\sqlexpress'

  options.AreaZoneMapping = False
  options.EuropeanPhaseShifters = True
  options.ENTSOEnaming = True
  options.RDFIDMapFile = '%s' % (map_file)
  options.GeneratingUnitType = odmsPy.EquipmentType.Unknown # GeneratingUnit

  # Iterate over the .raw files
  i = 0
  while i < 24:
    
    # Set import options
    options.InputFile = '%s%i_after_PF.raw' % (raw_prefix, i)
    options.Model = '%s%i' % (model_prefix, i)

    if not odmsPy.ImportExport().ImportPSSEModel(options):
      assert(False)

    # Set export options
    options.OutputFile = r'%s\%s.zip' % (output_dir, options.Model)
    options.PartialModel = False
    options.EnableProfiles = True
    options.IncludeEQ = False
    options.IncludeTP = True
    options.IncludeSV = True

    if not odmsPy.ImportExport().ExportCIMXML(options):
      assert(False)

    i += 1
