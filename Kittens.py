FIXES = {
    'archeology': 'geology',
}

COLORS = {
    'tabs': 'pink',
    'tech': 'deepskyblue',
    'jobs': 'blueviolet',
    'buildings': 'bisque4',
    'upgrades': 'darkolivegreen2',
    'crafts': 'chartreuse3',
}

TYPES = [
    'tabs',
    'tech',
    'jobs',
    'buildings',
    'upgrades',
    'crafts'
]

def get_types():
    return TYPES

def fix(name):
    return FIXES[name] if name in FIXES else name

def get_color(t):
    return COLORS[t] if t in COLORS else 'white'

class Tech:

    def __init__(self):
        self.all = [
            {
                'name': "calendar",
                'label': ("science.calendar.label"),
                'description': ("science.calendar.desc"),
                'effectDesc': ("science.calendar.effectDesc"),
                'prices': [{'name': "science", 'val': 30}],
                'unlocks': {
                    'tech': ["agriculture"],
                    'tabs': ["time"]
                },
                'flavor': ("science.calendar.flavor")
            },{
                'name': "agriculture",
                'label': ("science.agriculture.label"),
                'description': ("science.agriculture.desc"),
                'effectDesc': ("science.agriculture.effectDesc"),
                'prices': [{'name': "science", 'val': 100}],
                'unlocks': {
                    'buildings': ["barn"],
                    'tech': ["mining", "archery"],
                    'jobs': ["farmer"]
                },
                'flavor': ("science.agriculture.flavor")
            },{
                'name': "archery",
                'label': ("science.archery.label"),
                'description': ("science.archery.desc"),
                'effectDesc': ("science.archery.effectDesc"),
                'prices': [{'name': "science", 'val': 300}],
                'unlocks': {
                    'tech': ["animal"],
                    'jobs': ["hunter"]
                }
            },{
                'name': "mining",
                'label': ("science.mining.label"),
                'description': ("science.mining.desc"),
                'effectDesc': ("science.mining.effectDesc"),
                'prices': [{'name': "science", 'val': 500}],
                'unlocks': {
                    'buildings': ["mine", "workshop"],
                    'tech': ["metal"],
                    'upgrades': ["bolas"]
                },
                'flavor': ("science.mining.flavor")
            },{
                'name': "metal",
                'label': ("science.metal.label"),
                'description': ("science.metal.desc"),
                'effectDesc': ("science.metal.effectDesc"),
                'prices': [{'name': "science", 'val': 900}],
                'unlocks': {
                    'buildings': ["smelter"],
                    'upgrades': ["huntingArmor"]
                }
            },
            {
                'name': "animal",
                'label': ("science.animal.label"),
                'description': ("science.animal.desc"),
                'effectDesc': ("science.animal.effectDesc"),
                'prices': [{'name': "science", 'val': 500}],    #mostly does nothing, so price is lower
                'unlocks': {
                    'buildings': ["pasture", "unicornPasture"],
                    'tech': ["civil", "math", "construction"]
                    #'crafts': ["leather"]
                }
            },{
                #/*==============    NOT USED ANYMORE   ============*/
                'name': "brewery",
                'label': ("science.brewery.label"),
                'description': ("science.brewery.desc"),
                'effectDesc': ("science.brewery.effectDesc"),
                'prices': [{'name': "science", 'val': 1200 }]
            },
            #--------------------------------------------------
            {
                'name': "civil",
                'label': ("science.civil.label"),
                'description': ("science.civil.desc"),
                'effectDesc': ("science.civil.effectDesc"),
                'prices': [{'name': "science", 'val': 1500}],
                'unlocks': {
                    'tech': ["currency"]    #currency
                },
                'flavor': ("science.civil.flavor")
            },{
                'name': "math",
                'label': ("science.math.label"),
                'description': ("science.math.desc"),
                'effectDesc': ("science.math.effectDesc"),
                'prices': [{'name': "science", 'val': 1000}],
                'unlocks': {
                    'buildings': ["academy"],
                    'upgrades': ["celestialMechanics"],
                    'tabs': ["stats"]
                },
                'flavor': ("science.math.flavor")
            },{
                'name': "construction",
                'label': ("science.construction.label"),
                'description': ("science.construction.desc"),
                'effectDesc': ("science.construction.effectDesc"),
                'prices': [{'name': "science", 'val': 1300}],
                'unlocks': {
                    'buildings': ["logHouse", "warehouse", "lumberMill", "ziggurat"],
                    'tech': ["engineering"],
                    'upgrades': ["compositeBow", "advancedRefinement", "reinforcedSaw"]
                },
                'flavor': ("science.construction.flavor")
            },{
                'name': "engineering",
                'label': ("science.engineering.label"),
                'description': ("science.engineering.desc"),
                'effectDesc': ("science.engineering.effectDesc"),
                'prices': [{'name': "science", 'val': 1500}],
                'unlocks': {
                    'buildings': ["aqueduct"],
                    'tech': ["writing"]
                }
            },{
                'name': "currency",
                'label': ("science.currency.label"),
                'description': ("science.currency.desc"),
                'effectDesc': ("science.currency.effectDesc"),
                'prices': [{'name': "science", 'val': 2200}],
                'unlocks': {
                    'buildings': ["tradepost"],
                    'upgrades': ["goldOre"]
                }
            },{
                'name': "writing",
                'label': ("science.writing.label"),
                'description': ("science.writing.desc"),
                'effectDesc': ("science.writing.effectDesc"),
                'prices': [{'name': "science", 'val': 3600}],
                'unlocks': {
                    'buildings': ["amphitheatre"],
                    'tech': ["philosophy", "machinery", "steel"],
                    'upgrades': ["register"],
                    'crafts': ["parchment"]
                },
                'flavor': ("science.writing.flavor")
            },{
                'name': "philosophy",
                'label': ("science.philosophy.label"),
                'description': ("science.philosophy.desc"),
                'effectDesc': ("science.philosophy.effectDesc"),
                'prices': [{'name': "science", 'val': 9500}],
                'unlocks': {
                    'buildings': ["temple"],
                    'tech': ["theology"],
                    'crafts': ["compedium"]
                },
                'flavor': ("science.philosophy.flavor")
            },{
                'name': "machinery",
                'label': "Machinery",
                'description': "Previous advances in metal working and science give birth to the concept of a machine, a device with multiple moving parts. " +
                    "Machinery introduces a concept of automation which reduces routine operations",
                'effectDesc': "Unlocks Steamworks, Crossbows, Printing Press and Factory Automation.",
                'prices': [{'name': "science", 'val': 15000}],
                'unlocks': {
                    'buildings': ["steamworks"],
                    'upgrades': ["printingPress", "factoryAutomation", "crossbow"]
                }
            },{
                'name': "steel",
                'label': ("science.steel.label"),
                'description': ("science.steel.desc"),
                'effectDesc': ("science.steel.effectDesc"),
                'prices': [{'name': "science", 'val': 12000}],
                'unlocks': {
                    'upgrades': ["deepMining", "coalFurnace", "combustionEngine",
                                "reinforcedWarehouses", "steelAxe", "steelArmor"],
                    'crafts': ["steel"]
                }
            },{
                'name': "theology",
                'label': ("science.theology.label"),
                'description': ("science.theology.desc"),
                'effectDesc': ("science.theology.effectDesc"),
                'prices': [
                    {'name': "science", 'val': 20000},
                    {'name':     "manuscript", 'val': 35}
                ],
                'unlocks': {
                    'tech': ["astronomy", "cryptotheology"],
                    'jobs': ["priest"]
                },
                'upgrades': {
                    'buildings': ["temple"]
                },
                'flavor': ("science.theology.flavor")
            },{
                'name': "astronomy",
                'label': ("science.astronomy.label"),
                'description': ("science.astronomy.desc"),
                'effectDesc': ("science.astronomy.effectDesc"),
                'prices': [
                    {'name': "science", 'val': 28000},
                    {'name':     "manuscript", 'val': 65}
                ],
                'unlocks': {
                    'buildings': ["observatory"],
                    'tech': ["navigation"]
                }
            },{
                'name': "navigation",
                'label': ("science.navigation.label"),
                'description': ("science.navigation.desc"),
                'effectDesc': ("science.navigation.effectDesc"),
                'prices': [
                    {'name': "science", 'val': 35000},
                    {'name':     "manuscript", 'val': 100}
                ],
                'unlocks': {
                    'buildings': ["harbor"],
                    'tech': ["physics", "archeology", "architecture"],
                    'crafts': ["ship"],
                    'upgrades': ["caravanserai", "cargoShips", "astrolabe",
                                "titaniumMirrors", "titaniumAxe"]
                }
            },{
                'name': "architecture",
                'label': ("science.architecture.label"),
                'description': ("science.architecture.desc"),
                'effectDesc': ("science.architecture.effectDesc"),
                'prices': [
                    {'name': "science", 'val': 42000},
                    {'name':     "compedium", 'val': 10}
                ],
                'unlocks': {
                    'buildings': ["mansion", "mint"],
                    'tech': ["acoustics"]
                },
                'flavor': ("science.architecture.flavor")
            },{
                'name': "physics",
                'label': ("science.physics.label"),
                'description': ("science.physics.desc"),
                'effectDesc': ("science.physics.effectDesc"),
                'prices': [
                    {'name': "science", 'val': 50000},
                    {'name':     "compedium", 'val': 35}
                ],
                'unlocks': {
                    'tech': ["chemistry", "electricity", "metaphysics"],
                    'crafts': ["blueprint"],
                    'upgrades': ["pneumaticPress", "pyrolysis", "steelSaw"]
                }
            },{
                'name': "metaphysics",
                'label': ("science.metaphysics.label"),
                'description': ("science.metaphysics.desc"),
                'effectDesc': ("science.metaphysics.effectDesc"),
                'prices': [
                    {'name': "science", 'val': 55000},
                    {'name':     "unobtainium", 'val': 5}
                ],
            },{
                'name': "chemistry",
                'label': ("science.chemistry.label"),
                'description': ("science.chemistry.desc"),
                'effectDesc': ("science.chemistry.effectDesc"),
                'prices': [
                    {'name': "science", 'val': 60000},
                    {'name':     "compedium", 'val': 50}
                ],
                'unlocks': {
                    'buildings': ["calciner", "oilWell"],
                    'upgrades': ["alloyAxe", "alloyArmor", "alloyWarehouses", "alloyBarns"],
                    'crafts': ["alloy"]
                }
            },{
                'name': "acoustics",
                'label': ("science.acoustics.label"),
                'description': ("science.acoustics.desc"),
                'effectDesc': ("science.acoustics.effectDesc"),
                'prices': [
                    {'name': "science", 'val': 60000},
                    {'name':     "compedium", 'val': 60}
                ],
                'unlocks': {
                    'buildings': ["chapel"],
                    'tech': ["drama"]
                }
            },{
                'name': "drama",
                'label': ("science.drama.label"),
                'description': ("science.drama.desc"),
                'effectDesc': ("science.drama.effectDesc"),
                'prices': [
                    {'name': "science", 'val': 90000},
                    {'name':     "parchment", 'val': 5000}
                ],
            },{
                'name': "archeology",
                'label': ("science.archeology.label"),
                'description': ("science.archeology.desc"),
                'effectDesc': ("science.archeology.effectDesc"),
                'prices': [
                    {'name': "science", 'val': 65000},
                    {'name':     "compedium", 'val': 65}
                ],
                'unlocks': {
                    'buildings': ["quarry"],
                    'tech': ["biology"],
                    'jobs': ["geologist"],
                    'upgrades':["geodesy"]
                },
                'flavor': ("science.archeology.flavor")
            },{
                'name': "electricity",
                'label': ("science.electricity.label"),
                'description': ("science.electricity.desc"),
                'effectDesc': ("science.electricity.effectDesc"),
                'prices': [
                    {'name': "science", 'val': 75000},
                    {'name':     "compedium", 'val': 85}
                ],
                'unlocks': {
                    'buildings': ["magneto"],
                    'tech': ["industrialization"]
                },
                'flavor': ("science.electricity.flavor")
            },{
                'name': "biology",
                'label': ("science.biology.label"),
                'description': ("science.biology.desc"),
                'effectDesc': ("science.biology.effectDesc"),
                'prices': [
                    {'name': "science", 'val': 85000},
                    {'name':     "compedium", 'val': 100}
                ],
                'unlocks': {
                    'buildings': ["biolab"],
                    'tech': ["biochemistry"]
                }
            },{
                'name': "biochemistry",
                'label': ("science.biochemistry.label"),
                'description': ("science.biochemistry.desc"),
                'effectDesc': ("science.biochemistry.effectDesc"),
                'prices': [
                    {'name': "science", 'val': 145000},
                    {'name':     "compedium", 'val': 500}
                ],
                'unlocks': {
                    'tech': ["genetics"],
                    'upgrades': ["biofuel"]
                }
            },{
                'name': "genetics",
                'label': ("science.genetics.label"),
                'description': ("science.genetics.desc"),
                'effectDesc': ("science.genetics.effectDesc"),
                'prices': [
                    {'name': "science", 'val': 190000},
                    {'name':     "compedium", 'val': 1500}
                ],
                'unlocks': {
                    'upgrades': ["unicornSelection", "gmo"]
                }
            },{
                'name': "industrialization",
                'label': ("science.industrialization.label"),
                'description': ("science.industrialization.desc"),
                'effectDesc': ("science.industrialization.effectDesc"),
                'prices': [
                    {'name': "science", 'val': 100000},
                    {'name':     "blueprint", 'val': 25}
                ],
                'unlocks': {
                    'tech': ["mechanization", "metalurgy", "combustion"],
                    'upgrades': ["barges", "advancedAutomation", "logistics"]
                }
            },{
                'name': "mechanization",
                'label': ("science.mechanization.label"),
                'description': ("science.mechanization.desc"),
                'effectDesc': ("science.mechanization.effectDesc"),
                'prices': [
                    {'name': "science", 'val': 115000},
                    {'name':     "blueprint", 'val': 45}
                ],
                'unlocks': {
                    'buildings': ["factory"],
                    'tech': ["electronics"],
                    'crafts': ["concrate"],
                    'upgrades': ["pumpjack", "strenghtenBuild"],
                    'jobs': ["engineer"]
                }
            },{
                'name': "metalurgy",
                'label': ("science.metalurgy.label"),
                'description': ("science.metalurgy.desc"),
                'effectDesc': ("science.metalurgy.effectDesc"),
                'prices': [
                    {'name': "science", 'val': 125000},
                    {'name':     "blueprint", 'val': 60}
                ],
                'unlocks': {
                    'upgrades': ["electrolyticSmelting", "oxidation", "retorting", "miningDrill"]
                }
            },{
                'name': "combustion",
                'label': ("science.combustion.label"),
                'description': ("science.combustion.desc"),
                'effectDesc': ("science.combustion.effectDesc"),
                'prices': [
                    {'name': "science", 'val': 115000},
                    {'name':     "blueprint", 'val': 45}
                ],
                'unlocks': {
                    'upgrades': ["offsetPress", "fuelInjectors", "oilRefinery"],
                    'tech': ["ecology"]
                }
            },
            {
                'name': "ecology",
                'label': ("science.ecology.label"),
                'description': ("science.ecology.desc"),
                'effectDesc': ("science.ecology.effectDesc"),
                'prices': [
                    {'name': "science", 'val': 125000},
                    {'name':     "blueprint", 'val': 55}
                ],
                'unlocks': {
                    'stages': [{'bld':"pasture",'stage':1}] # Solar Farm
                }
            },
            {
                'name': "electronics",
                'label': ("science.electronics.label"),
                'description': ("science.electronics.desc"),
                'effectDesc': ("science.electronics.effectDesc"),
                'prices': [
                    {'name': "science", 'val': 135000},
                    {'name':     "blueprint", 'val': 70}
                ],
                'unlocks': {
                    'stages': [{'bld':"amphitheatre",'stage':1}], # Broadcast Tower
                    'tech': ["nuclearFission", "rocketry", "robotics"],
                    'upgrades': ["cadSystems", "refrigeration", "seti", "factoryLogistics", "factoryOptimization", "internet"]
                }
            },{
                'name': "robotics",
                'label': ("science.robotics.label"),
                'description': ("science.robotics.desc"),
                'effectDesc': ("science.robotics.effectDesc"),
                'prices': [
                    {'name': "science", 'val': 140000},
                    {'name':     "blueprint", 'val': 80}
                ],
                'unlocks': {
                    'stages': [{'bld':"aqueduct",'stage':1}], # Hydro Plant
                    'upgrades': ["steelPlants", "rotaryKiln", "assistance", "factoryRobotics"],
                    'crafts': ["tanker"],
                    'tech': ["ai"],
                }
            },{
                'name': "ai",
                'label': ("science.ai.label"),
                'description': ("science.ai.desc"),
                'effectDesc': ("science.ai.effectDesc"),
                'prices': [
                    {'name': "science", 'val': 250000},
                    {'name':     "blueprint", 'val': 150}
                ],
                'unlocks': {
                    'upgrades': ["neuralNetworks", "aiEngineers"],
                    'buildings': ["aiCore"],
                    'tech': ["quantumCryptography"]
                }
            },{
                'name': "quantumCryptography",
                'label': ("science.quantumCryptography.label"),
                'description': ("science.quantumCryptography.desc"),
                'effectDesc': ("science.quantumCryptography.effectDesc"),
                'prices': [
                    {'name': "science", 'val': 1250000},
                    {'name':     "relic", 'val': 1024}
                ],
                'unlocks': {
                }
            },{
                'name': "nuclearFission",
                'label': ("science.nuclearFission.label"),
                'description': ("science.nuclearFission.desc"),
                'effectDesc': ("science.nuclearFission.effectDesc"),
                'prices': [
                    {'name': "science", 'val': 150000},
                    {'name':     "blueprint", 'val': 100}
                ],
                'unlocks': {
                    'buildings': ["reactor"],
                    'tech': ["nanotechnology", "particlePhysics"],
                    'upgrades': ["reactorVessel", "nuclearSmelters"]
                }
            },{
                'name': "rocketry",
                'label': ("science.rocketry.label"),
                'description': ("science.rocketry.desc"),
                'effectDesc': ("science.rocketry.effectDesc"),
                'prices': [
                    {'name': "science", 'val': 175000},
                    {'name':     "blueprint", 'val': 125}
                ],
                'unlocks': {
                    'tech': ["sattelites", "oilProcessing"],
                    'tabs': ["space"],
                    'upgrades': ["oilDistillation"]
                }
            }, {
                'name': "oilProcessing",
                'label': ("science.oilProcessing.label"),
                'description': ("science.oilProcessing.desc"),
                'effectDesc': ("science.oilProcessing.effectDesc"),
                'prices': [
                    {'name': "science", 'val': 215000},
                    {'name':     "blueprint", 'val': 150}
                ],
                'unlocks': {
                    'crafts': ["kerosene"],
                    'upgrades': [ "factoryProcessing" ]
                }
            },{
                'name': "sattelites",
                'label': ("science.sattelites.label"),
                'description': ("science.sattelites.desc"),
                'effectDesc': ("science.sattelites.effectDesc"),
                'prices': [
                    {'name': "science", 'val': 190000},
                    {'name':     "blueprint", 'val': 125}
                ],
                'unlocks': {
                    'tech': ["orbitalEngineering" ],
                    'upgrades': [ "photolithography" ]
                },
                'flavor': ("science.sattelites.flavor")
            },{
                'name': "orbitalEngineering",
                'label': ("science.orbitalEngineering.label"),
                'description': ("science.orbitalEngineering.desc"),
                'effectDesc': ("science.orbitalEngineering.effectDesc"),
                'prices': [
                    {'name': "science", 'val': 250000},
                    {'name':     "blueprint", 'val': 250}
                ],
                'unlocks': {
                    'tech': ["exogeology", "thorium"],
                    'upgrades': ["hubbleTelescope", "satelliteRadio", "astrophysicists", "solarSatellites", "spaceEngineers"]
                }
            },{
                'name': "thorium",
                'label': ("science.thorium.label"),
                'description': ("science.thorium.desc"),
                'effectDesc': ("science.thorium.effectDesc"),
                'prices': [
                    {'name': "science", 'val': 375000},
                    {'name':     "blueprint", 'val': 375}
                ],
                'unlocks': {
                    'crafts': ["thorium"],
                    'upgrades': ["thoriumReactors", "thoriumEngine"]
                }
            },{
                'name': "exogeology",
                'label': ("science.exogeology.label"),
                'description': ("science.exogeology.desc"),
                'effectDesc': ("science.exogeology.effectDesc"),
                'prices': [
                    {'name': "science", 'val': 275000},
                    {'name':     "blueprint", 'val': 250}
                ],
                'unlocks': {
                    'tech': ["advExogeology"],
                    'upgrades': ["unobtainiumReflectors", "unobtainiumHuts", "unobtainiumDrill", "hydroPlantTurbines", "storageBunkers"]
                }
            },{
                'name': "advExogeology",
                'label': ("science.advExogeology.label"),
                'description': ("science.advExogeology.desc"),
                'effectDesc': ("science.advExogeology.effectDesc"),
                'prices': [
                    {'name': "science", 'val': 325000},
                    {'name':     "blueprint", 'val': 350}
                ],
                'unlocks': {
                    #'upgrades': ["eludiumCracker", "eludiumReflectors", "eludiumHuts", "mWReactor" /*, "eludiumDrill"*/],
                    'upgrades': ["eludiumCracker", "eludiumReflectors", "eludiumHuts", "mWReactor"],
                    'crafts': ["eludium"]
                }
            },
            {
                'name': "nanotechnology",
                'label': ("science.nanotechnology.label"),
                'description': ("science.nanotechnology.desc"),
                'effectDesc': ("science.nanotechnology.effectDesc"),
                'prices': [
                    {'name': "science", 'val': 200000},
                    {'name':     "blueprint", 'val': 150}
                ],
                'unlocks': {
                    'tech': ["superconductors"],
                    'upgrades': ["augumentation", "nanosuits", "photovoltaic", "fluidizedReactors"]
                }
            },{
                'name': "superconductors",
                'label': ("science.superconductors.label"),
                'description': ("science.superconductors.desc"),
                'effectDesc': ("science.superconductors.effectDesc"),
                'prices': [
                    {'name': "science", 'val': 225000},
                    {'name':     "blueprint", 'val': 175}
                ],
                'unlocks': {
                    'upgrades': ["coldFusion", "spaceManufacturing"],
                    'tech': ["antimatter"]
                }
            },{
                'name': "antimatter",
                'label': ("science.antimatter.label"),
                'description': ("science.antimatter.desc"),
                'effectDesc': ("science.antimatter.effectDesc"),
                'prices': [
                    {'name': "science", 'val': 500000},
                    {'name': "relic",   'val': 1}
                ],
                'unlocks': {
                    'upgrades': ["amReactors", "amBases", "amDrive", "amFission"],
                    'tech': ["terraformation"]
                }
            },{
                'name': "terraformation",
                'label': ("science.terraformation.label"),
                'description': ("science.terraformation.desc"),
                'effectDesc': ("science.terraformation.effectDesc"),
                'prices': [
                    {'name': "science", 'val': 750000},
                    {'name': "relic",   'val': 5}
                ],
                'unlocks': {
                    'tech': ["hydroponics"]
                }
            },{
                'name': "hydroponics",
                'label': ("science.hydroponics.label"),
                'description': ("science.hydroponics.desc"),
                'effectDesc': ("science.hydroponics.effectDesc"),
                'prices': [
                    {'name': "science", 'val': 1000000},
                    {'name': "relic",   'val': 25}
                ]
            },{
                'name': "particlePhysics",
                'label': ("science.particlePhysics.label"),
                'description': ("science.particlePhysics.desc"),
                'effectDesc': ("science.particlePhysics.effectDesc"),
                'prices': [
                    {'name': "science", 'val': 185000},
                    {'name':     "blueprint", 'val': 135}
                ],
                'unlocks': {
                    'buildings': ["accelerator"],
                    'tech': ["chronophysics", "dimensionalPhysics"],
                    'upgrades': ["enrichedUranium", "railgun"]
                }
            },{
                'name': "dimensionalPhysics",
                'label': ("science.dimensionalPhysics.label"),
                'description': ("science.dimensionalPhysics.desc"),
                'effectDesc': ("science.dimensionalPhysics.effectDesc"),
                'prices': [
                    {'name': "science", 'val': 235000}
                ],
                'unlocks': {
                    'upgrades': ["energyRifts", "lhc"]
                }
            },{
                'name': "chronophysics",
                'label': ("science.chronophysics.label"),
                'description': ("science.chronophysics.desc"),
                'effectDesc': ("science.chronophysics.effectDesc"),
                'prices': [
                    {'name': "science", 'val': 250000},
                    {'name':     "timeCrystal", 'val': 5}
                ],
                'unlocks': {
                    'buildings': ["chronosphere"],
                    'tech': ["tachyonTheory"],
                    'upgrades': ["stasisChambers", "fluxCondensator"]
                }
            },{
                'name': "tachyonTheory",
                'label': ("science.tachyonTheory.label"),
                'description': ("science.tachyonTheory.desc"),
                'effectDesc': ("science.tachyonTheory.effectDesc"),
                'prices': [
                    {'name': "science", 'val': 750000},
                    {'name':     "timeCrystal", 'val': 25},
                    {'name': "relic",   'val': 1}
                ],
                'unlocks': {
                    'tech': ["voidSpace"],
                    'upgrades': ["tachyonAccelerators", "chronoforge", "chronoEngineers"]
                }
            },{
                'name': "cryptotheology",
                'label': ("science.cryptotheology.label"),
                'description': ("science.cryptotheology.desc"),
                'effectDesc': ("science.cryptotheology.effectDesc"),
                'prices': [
                    {'name': "science", 'val': 650000},
                    {'name': "relic",   'val': 5}
                ],
                'unlocks': {
                    'upgrades': ["relicStation"]
                }
            },{
                'name': "voidSpace",
                'label': ("science.voidSpace.label"),
                'description': ("science.voidSpace.desc"),
                'effectDesc': ("science.voidSpace.effectDesc"),
                'prices': [
                    {'name': "science", 'val': 800000},
                    {'name':     "timeCrystal", 'val': 30},
                    {'name': "void",   'val': 100}
                ],
                'unlocks': {
                    'tech': ["paradoxalKnowledge"],
                    'upgrades': ["voidAspiration"],
                    'voidSpace': ["cryochambers"],
                    'challenges': ["atheism"]
                }
            },{
                'name': "paradoxalKnowledge",
                'label': ("science.paradoxalKnowledge.label"),
                'description': ("science.paradoxalKnowledge.desc"),
                'effectDesc': ("science.paradoxalKnowledge.effectDesc"),
                'prices': [
                    {'name': "science", 'val': 1000000},
                    {'name':     "timeCrystal", 'val': 40},
                    {'name': "void",   'val': 250}
                ],
                'unlocks': {
                    'chronoforge': ["ressourceRetrieval"],
                    'voidSpace': ["chronocontrol"],
                    'upgrades': ["distorsion"]
                }
            }
        ]
