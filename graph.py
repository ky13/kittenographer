#!/usr/bin/env python3

import Kittens
from graphviz import Digraph

dot = Digraph(
    format='svg',
    graph_attr={'layout':'dot'},
    node_attr={'shape':'box', 'style':'filled'}
)

for tech in Kittens.Tech().all:
    tech_name = Kittens.fix(tech['name'])
    dot.node(tech_name, tech_name, fillcolor=Kittens.get_color('tech'))
    if "unlocks" in tech and "tech" in tech['unlocks']:
        for t in Kittens.get_types():
            if t in tech['unlocks']:
                for name in tech['unlocks'][t]:
                    name = Kittens.fix(name)
                    dot.node(name, name, fillcolor=Kittens.get_color(t))
                    dot.edge(tech_name, name)

dot.render('tree')

