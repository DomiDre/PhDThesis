#!/bin/bash
shopt -s expand_aliases
source ~/.bash_aliases

sared ES_S16_30K_FC_7Oe_Remanence.h5 -roix 700 1200 -roiy 300 1100 -beamcenter 840 -sdd 2500 -project -save_to_bd_in_aiaf
sared ES_S16_30K_FC_7300Oe.h5 -roix 700 1200 -roiy 300 1100 -beamcenter 840 -sdd 2500 -project -save_to_bd_in_aiaf
sared ES_S16_30K_ZFC_7Oe_Remanence.h5 -roix 700 1200 -roiy 300 1100 -beamcenter 858 -sdd 2500 -project -save_to_bd_in_aiaf
sared ES_S16_30K_ZFC_7Oe_Virgin.h5 -roix 700 1200 -roiy 300 1100 -beamcenter 858 -sdd 2500 -project -save_to_bd_in_aiaf
sared ES_S16_30K_ZFC_7300Oe.h5 -roix 700 1200 -roiy 300 1100 -beamcenter 858 -sdd 2500 -project -save_to_bd_in_aiaf

