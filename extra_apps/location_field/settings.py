from django.conf import settings

LOCATION_FIELD_PATH = settings.STATIC_URL + 'location_field'

LOCATION_FIELD = {
    'map.provider': 'google',
    'map.zoom': 12,
    'map.center': '114.0160,22.72645',

    'search.provider': 'google',
    'search.suffix': '',
    'map.widget_width': '500px',
    'map.widget_height': '250px',

    # Google
    'provider.google.api': '//maps.google.com/maps/api/js',
    'provider.google.api_key': '',
    'provider.google.map_type': 'ROADMAP',

    # Mapbox
    'provider.mapbox.access_token': '',
    'provider.mapbox.max_zoom': 18,
    'provider.mapbox.id': 'mapbox.streets',

    # OpenStreetMap
    'provider.openstreetmap.max_zoom': 20,

    # misc
    'resources.root_path': LOCATION_FIELD_PATH,
    'resources.media': {
        'js': [
            LOCATION_FIELD_PATH + '/js/form.js',
        ],
    },
}
