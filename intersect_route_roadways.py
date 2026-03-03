"""
intersect_route_roadways.py

Creates point features at every intersection between a recommended route
line and TxDOT roadways.

Inputs
------
recommended_route : str
    Path to the recommended route feature class (line geometry).
roadways : str
    Path to the TxDOT roadways feature class (line geometry).
output_points : str
    Path for the output point feature class.

Usage
-----
    Run from ArcGIS Pro Python window, a standalone Python environment with
    arcpy, or publish as a script tool.

    python intersect_route_roadways.py <recommended_route> <roadways> <output_points>
"""

import arcpy
import sys


def create_intersection_points(recommended_route, roadways, output_points):
    """Find every intersection between the recommended route and the
    roadways layer and write each one as a point feature.

    Parameters
    ----------
    recommended_route : str
        Path to the recommended route line feature class.
    roadways : str
        Path to the TxDOT roadways line feature class.
    output_points : str
        Path for the output point feature class that will be created.

    Returns
    -------
    str
        Path to the output point feature class.
    """

    # Validate inputs exist
    if not arcpy.Exists(recommended_route):
        raise ValueError(
            f"Recommended route does not exist: {recommended_route}"
        )
    if not arcpy.Exists(roadways):
        raise ValueError(f"Roadways layer does not exist: {roadways}")

    # Use the Intersect tool to find point intersections between the two
    # line feature classes.  Setting output_type to "POINT" ensures that
    # only point geometries are produced (one per crossing).
    arcpy.analysis.Intersect(
        in_features=[recommended_route, roadways],
        out_feature_class=output_points,
        output_type="POINT",
    )

    count = int(arcpy.management.GetCount(output_points)[0])
    arcpy.AddMessage(f"Created {count} intersection point(s) at: {output_points}")

    return output_points


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print(
            "Usage: python intersect_route_roadways.py "
            "<recommended_route> <roadways> <output_points>"
        )
        sys.exit(1)

    recommended_route = sys.argv[1]
    roadways = sys.argv[2]
    output_points = sys.argv[3]

    arcpy.env.overwriteOutput = True

    create_intersection_points(recommended_route, roadways, output_points)
