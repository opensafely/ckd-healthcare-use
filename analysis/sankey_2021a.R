#Load packages
library(tidyverse)
library(readr)
library(webshot)
library(phantomjs)
#Set local working directory
setwd("C:/Users/viymah/Dropbox/PhD/health economics/outputs/release-01GYZGKP9CRD1BJCW60B17P9WF/release/26042023/sankey")
# Read CSV files with nodes (CKD groups with a specified ID #) and edges (transitions between each ID # 
# with weights for each transition)
# NB - fileEncoding="UTF-8-BOM" added because nodes kept prefixing id with "ï.." otherwise
nodes <- read.csv("nodes.csv", fileEncoding="UTF-8-BOM")
edges <- read_csv("edges_2021a.csv")
library("networkD3")
nodes_d3 <- mutate(nodes, id = id - 1)
edges_d3 <- mutate(edges, from = from - 1, to = to - 1)
# progression_2021a = object which can then be saved
progression_2021a <- sankeyNetwork(
  Links = edges_d3, Nodes = nodes_d3, 
  Source = "from", Target = "to", 
  NodeID = "label", Value = "weight", 
  fontSize = 36, unit = "Letter(s)")
# Save as HTML file
saveNetwork(progression_2021a, "2021a.html")
# Export from HTML to PNG
webshot::webshot("2021a.html","2021a.png", vwidth = 1000, vheight = 900)