"""
LIST every instance of a database connection in an ArcGIS Pro (APRX) project file.

This file has the biz logic for the tool.

@author: Brian Wilson <bwilson@clatsopcounty.gov>
"""
import os
import pprint
import arcpy

# This is for development, so that you can edit code while running in ArcGIS Pro.
import importlib


def list_database_connections(aprx : object) -> list :
    """
        Input: an aprx object 
        Returns: a list of information about the databases in the APRX.
    """
    d_databases = dict()
    results = list()
    for map in aprx.listMaps('*'):
        count = 0
        for lyr in map.listLayers():
            count += 1
            try:
                dataSource = lyr.dataSource
            except Exception as e:
                # This layer has no datasource, so skip it.
                continue

            this = dict()
            this['map'] = map.name

            if lyr.isGroupLayer:
                this["layerType"] = "group"
                this["layer"] = lyr.name

            elif lyr.isBasemapLayer:
                this["layerType"] = "basemap"
                this["layer"] = lyr.name

            elif lyr.isWebLayer: 
                this["layerType"] = "webLayer"
                this["layer"] = lyr.name
                continue

            elif lyr.isBroken:
                this["layerType"] = "**BROKEN**"
                this["layer"] = lyr.name

            else:
                this["layerType"] = "other"
                this["layer"] = lyr.name

            try:
                properties = lyr.connectionProperties
            except Exception as e:
                print(e)
                continue

            try:
                if 'connection_info' in properties:
                    p = properties['connection_info']
                    if 'server' in p:
                        this["server"] = p['server']
                    if 'database' in p:
                        db = p['database']
                        this["database"] = db
                        if db in d_databases:
                            d_databases[db] += 1
                        else:
                            d_databases[db] = 1
                if 'db_connection_properties' in p:
                    this["db_connection_properties"] = p['db_connection_properties'] 
                if 'authentication_mode' in p:
                    print(f"    authentication mode: {p['authentication_mode']}")
                #if 'instance' in p:
                #    print(f"    instance: {p['instance']}")
                if 'version' in p:
                    this['version'] = p['version']
                if 'user' in p:
                    print(f"    user: {p['user']} / password: {p['password']}")

            except Exception as e:
                print(f"  {count} {lyr.name} -- Error={e}")
                pass
        results.append(this)

    for k in d_databases:
        print(f"  {k} {d_databases[k]}")

    return results
    
# =============================================================================
if __name__ == "__main__":

    aprx_file = "c:\\Users\\bwilson\\Documents\\source\\basemap\\basemap.aprx"
    #aprx_file = "C:\\Users\\bwilson\\Documents\\ArcGIS\\Projects\\MyProject\\MyProject.aprx"
    results = None
    try:
        aprx = arcpy.mp.ArcGISProject(aprx_file)
        results = list_database_connections(aprx)
    except Exception as e:
        arcpy.AddError("Fail. %s" % e)

    pprint.pprint(results)

    print("Done!")

# That's all!
