#!/usr/bin/env python

import argparse
from core.projects.LangProject import LangProject
from core.projects.MathProject import MathProject
from core.projects.ChartProject import ChartProject
from core.projects.TimeProject import TimeProject
from core.projects.ClosureProject import ClosureProject
from core.projects.MockitoProject import MockitoProject

from core.tools.Ranking import Ranking
from core.tools.NopolPC import NopolPC
from core.tools.NopolC import NopolC
from core.tools.Nopol import Nopol
from core.tools.Brutpol import Brutpol
from core.tools.BrutpolPC import BrutpolPC
from core.tools.BrutpolC import BrutpolC
from core.tools.Brutpol import Brutpol
from core.tools.Astor import Astor
from core.tools.Kali import Kali
from core.tools.AdqFix import AdqFix



def initParser():
    parser = argparse.ArgumentParser(description='Run tools on defect4j with grid5000')
    parser.add_argument('-project', required=True, help='Which project (all, math, lang, time)')
    parser.add_argument('-tool', required=True, help='Which tool (nopol, ranking, ...)')
    parser.add_argument('-id',  help='Bug id')
    return parser.parse_args()

args = initParser()
project = None
tool = None
id = int(args.id)
if args.project.lower() == "Lang".lower():
    project = LangProject()
elif args.project.lower() == "Math".lower():
    project = MathProject()
elif args.project.lower() == "Chart".lower():
    project = ChartProject()
elif args.project.lower() == "Time".lower():
    project = TimeProject()
elif args.project.lower() == "Closure".lower():
    project = ClosureProject()
elif args.project.lower() == "Mockito".lower():
    project = MockitoProject()

if args.tool.lower() == "NopolPC".lower():
    tool = NopolPC()
elif args.tool.lower() == "NopolC".lower():
    tool = NopolC()
elif args.tool.lower() == "Nopol".lower():
    tool = Nopol() 
elif args.tool.lower() == "Brutpol".lower():
    tool = Brutpol() 
elif args.tool.lower() == "BrutpolPC".lower():
    tool = BrutpolPC()
elif args.tool.lower() == "BrutpolC".lower():
    tool = BrutpolC() 
elif args.tool.lower() == "Ranking".lower():
    tool = Ranking()     
elif args.tool.lower() == "Genprog".lower():
    tool = Astor()
elif args.tool.lower() == "Kali".lower():
    tool = Kali()
elif args.tool.lower() == "adqfix".lower():
    tool = AdqFix()
        
# tool.run(project, id)
tool.initTask(project, id);
