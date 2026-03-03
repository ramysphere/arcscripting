# arcscripting

ArcGIS Python scripts for geospatial analysis.

## intersect\_route\_roadways.py

Creates a point feature for every intersection between a recommended route line and the TxDOT roadways layer.

### Requirements

- ArcGIS Pro with a valid license (provides `arcpy`)

### Inputs

| Parameter | Description |
|---|---|
| `recommended_route` | Path to the recommended route feature class (line geometry) |
| `roadways` | Path to the TxDOT roadways feature class (line geometry) |
| `output_points` | Path for the output point feature class |

### Usage

```bash
python intersect_route_roadways.py <recommended_route> <roadways> <output_points>
```

**Example:**

```bash
python intersect_route_roadways.py ^
    "C:/Data/Project.gdb/RecommendedRoute" ^
    "C:/Data/Project.gdb/TxDOT_Roadways" ^
    "C:/Data/Project.gdb/IntersectionPoints"
```

The script can also be imported as a module:

```python
from intersect_route_roadways import create_intersection_points

create_intersection_points(
    recommended_route="C:/Data/Project.gdb/RecommendedRoute",
    roadways="C:/Data/Project.gdb/TxDOT_Roadways",
    output_points="C:/Data/Project.gdb/IntersectionPoints",
)
```
