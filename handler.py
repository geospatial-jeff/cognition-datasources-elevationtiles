from datasources import Manifest

def ElevationTiles(event, context):
    manifest = Manifest()
    manifest['ElevationTiles'].search(**event)
    response = manifest.execute()
    return response


