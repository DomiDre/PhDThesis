#!/bin/bash
shopt -s expand_aliases
source ~/.bash_aliases

sared ES_S16_300K_4mT.h5 -project -save_to_bd_in_aiaf
sared ES_S16_300K_500mT.h5 -project -save_to_bd_in_aiaf
sared ES_S16_300K_4mT_Remanence.h5 -project -save_to_bd_in_aiaf
