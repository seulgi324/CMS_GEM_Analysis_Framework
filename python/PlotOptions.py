from optparse import OptionParser

parser=OptionParser()

parser.add_option('-f','--file',action="append",dest='file',type=str)
parser.add_option('--OutputName',action="store",dest="OutputName",type=str,default="Plotconfig",help="Set Output file name, default is: PlotConfig")
parser.add_option('--SelectSheetNum',action="store",dest="SelectSheetNum",type=int,default=0,help="Select the Excel sheet for reading, default is: 0 ")
parser.add_option('--SelectColumnX',action="store",dest="SelectColumnX",type=int,default=0,help= "Select Column number for X data, default value is 0 (counting starts from 0)")
parser.add_option('--SelectColumnY',action="store",dest="SelectColumnY",type=int,default=0,help= "Select Column number for Y data, default value is 0 (counting starts from 0)")
parser.add_option('--SelectRowStart',action="store",dest="SelectRowStart",type=int,default=1,help= "Select the first Row for reading, default is 1 (counting starts from 0)")
parser.add_option('--SelectRowEnd',action="store",dest="SelectRowEnd",type=int,default=60,help= "Select the last Row for reading, default is 61 (counting starts from 0)")
parser.add_option('--AxisNDiv',action="store",dest="AxisNDiv",type=str,default="508,510",help="Set Axis Ndivisions X,Y (default is: 508,510)")
parser.add_option('--CanvDim',action="store",dest="CanvDim",type=str,default="1000,1000",help="Set Canvas Dimensions X,Y (default is: 1000,1000)")
parser.add_option('--CanvDrawOpt',action="store",dest="CanvDrawOpt",type=str,default="APE1",help="Set Draw Option (default is: APE1)")
parser.add_option('--CanvGridXY',action="store",dest="CanvGridXY",type=str,default="false,false",help="Set GridXY option (default: false,false)")
parser.add_option('--LatexLines', action="append", type=str, dest="LatexLines", help= "Add an entry to the LatexLines list following syntax: 'Coord_PadX,Coord_PadY, text'", metavar="latexLines")
parser.add_option('--CanvLegDimX',action="store",dest="CanvLegDimX",type=str,default="0.20,0.60",help="Set X Legend Dimensions") 
parser.add_option('--CanvLegDimY',action="store",dest="CanvLegDimY",type=str,default="0.56,0.92",help="Set Y Legend Dimensions") 
parser.add_option('--CanvLegDraw',action="store",dest="CanvLegDraw",type=str,default="true",help="Set Legend Draw Option (dedault: true)") 
parser.add_option('--CanvLogXY',action="store",dest="CanvLogXY",type=str,default="false,false",help="Set Canvas LogXY options (default: false,false)") 
parser.add_option('--CanvLogoPos',action="store",dest="CanvLogoPos",type=str,default="0",help="Set Logo Position (Default: 0 , Other Options: 11, 22, 33") 
parser.add_option('--CanvLogoPrelim',action="store",dest="CanvLogoPrelim",type=str,default="true",help="Set Logo Preliminary true or false (default is true)") 
parser.add_option('--CanvMarginTop',action="store",dest="CanvMarginTop",type=str,default="0.08",help="Set Canvas Margin Top (default is 0.08)") 
parser.add_option('--CanvMarginBot',action="store",dest="CanvMarginBot",type=str,default="0.14",help="Set Canvas Margin Bottom (default is 0.14)") 
parser.add_option('--CanvMarginLf',action="store",dest="CanvMarginLf",type=str,default="0.16",help="Set Canvas Margin Left (default is 0.16)") 	
parser.add_option('--CanvMarginRt',action="store",dest="CanvMarginRt",type=str,default="0.06",help="Set Canvas Margin Right (default is 0.06)") 
parser.add_option('--CanvPlotType',action="store",dest="CanvPlotType",type=str,default="TGraphErrors",help="Set the Canvas Plot type (default is TGraphErrors)") 
parser.add_option('--CanvTitleX',action="store",dest="CanvTitleX",type=str,default="",help="Set Xaxis title, example: Divider Current #left(#muA#right)")
parser.add_option('--CanvTitleY',action="store",dest="CanvTitleY",type=str,default="",help="Set Yaxis title, example:Applied Voltage #left(kV#right)")
parser.add_option('--CanvRangeX',action="store",dest="CanvRangeX",type=str,default="0,1000",help="Set the X-Range of the Canvas (default is 0,1000)") 
parser.add_option('--CanvRangeY',action="store",dest="CanvRangeY",type=str,default="0,7",help="Set the Y-Range of the Canvas (default is 0,7)") 
parser.add_option('--CanvTitleOffsetX',action="store",dest="CanvTitleOffsetX",type=str,default="1.0",help="Set the X-Offset of the Canvas Title (default is 1.0)") 
parser.add_option('--CanvTitleOffsetY',action="store",dest="CanvTitleOffsetY",type=str,default="0.8",help="Set the Y-offset of the Canvas Title (default is 0.8)") 
parser.add_option('--CanvName',action="store",dest="CanvName",type=str,default="LS2_Detectors",help="Set Canvas Name, Default is: LS2_Detectors")
parser.add_option('--YaxisScale',action="store_true",default=False,help="If YaxisScale option is used the Y axis is plotted in kUnit. Default is: False")
parser.add_option('--SetErrX',action="store_true",default=False,help="Set Error option true (for X axis) ")
parser.add_option('--SetErrY',action="store_true",default=False,help="Set Error option true (for Y axis)")
parser.add_option('--SelectColumnErrX',action="store",dest="SelectColumnErrX",type=int,default=0,help="If SetErrX=True choose the Column for XError, Default is: 0")
parser.add_option('--SelectColumnErrY',action="store",dest="SelectColumnErrY",type=int,default=0,help="If SetErrY=True choose the Column for YError, Default is: 0")
parser.add_option('--PlotLineSize',action="store",dest="PlotLineSize",type=str,default="1",help="Set Plot Line Size (default is: 1)")
parser.add_option('--PlotLineStyle',action="store",dest="PlotLineStyle",type=str,default="1",help="Set Plot Line Style (default is: 1)")
parser.add_option('--PlotMarkerSize',action="store",dest="PlotMarkerSize",type=str,default="0.8",help="Set Plot Marker Size (default is: 0.8)")
parser.add_option('--Fit',default=False,action='store_true',help="if it is used the header parameters for the fit are created")
parser.add_option('--FitFormula',action="store",dest="FitFormula",type=str,default="[0]",help="Set the fit formula e.g. [0]*x^2+[1]")
parser.add_option('--FitLineSize',action="store",dest="FitLineSize",type=str,default="1",help="Set Fit Line Size, default is: 1")
parser.add_option('--FitLineStyle',action="store",dest="FitLineStyle",type=str,default="1",help="Set Fit Line Style, default is: 1")
parser.add_option('--FitOption',action="store",dest="FitOption",type=str,default="R",help="Set Fit Option, default is: R")
parser.add_option('--FitParamIGuess',action="store",dest="FitParamIGuess",type=str,default="0",help="Set Fit Parameters initial values, example: 10,15 (for a fit function with two parameters)")
parser.add_option('--FitPerform',action="store",dest="FitPerform",type=str,default="true",help="if true (default) perform a fit to the TObject defined in the [BEGIN_PLOT]header this [BEGIN_FIT] header is found in")
parser.add_option('--FitRange',action="store",dest="FitRange",type=str,default="0,1",help="Set the Fit range, default is 0,1")
