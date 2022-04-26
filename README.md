# cellular-life-simulation
![Tests](https://github.com/Rafal-Majewski/cellular-life-simulation/actions/workflows/tests.yml/badge.svg)

## config.json
```json
{
	"game": {
		"fps": 60,
		"world": {
			"quadtree": {
				"chunks": {
					"minSize": {
						"width": 3,
						"height": 3
					},
					"maxSize": {
						"width": 50,
						"height": 50
					}
				}
			},
			"size": {
				"width": 800,
				"height": 600
			},
			"atoms": {
				"air": {
					"radius": 10,
					"color": {
						"r": 0,
						"g": 0,
						"b": 255
					},
					"mass": 0.1
				},
				"cells": {
					"scale": 5
				}
			}
		}
	}
}
```