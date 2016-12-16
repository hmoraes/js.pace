from fanstatic import Library, Resource, Group

library = Library('pace', 'resources')

pace_js = Resource(library, 'js/pace.js', minified='js/pace.min.js')

pace_barber_shop_css = Resource(library, 'css/pace-barber-shop.css')
pace_center_atom_css = Resource(library, 'css/pace-center-atom.css')
pace_center_simple_css = Resource(library, 'css/pace-center-simple.css')
pace_flash_css = Resource(library, 'css/pace-flash.css')
pace_macosx_css = Resource(library, 'css/pace-macosx.css')
pace_big_counter_css = Resource(library, 'css/pace-big-counter.css')
pace_center_circle_css = Resource(library, 'css/pace-center-circle.css')
pace_corner_indicator_css = Resource(library, 'css/pace-corner-indicator.css')
pace_flat_top_css = Resource(library, 'css/pace-flat-top.css')
pace_minimal_css = Resource(library, 'css/pace-minimal.css')
pace_bounce_css = Resource(library, 'css/pace-bounce.css')
pace_center_radar_css = Resource(library, 'css/pace-center-radar.css')
pace_fill_left_css = Resource(library, 'css/pace-fill-left.css')
pace_loading_bar_css = Resource(library, 'css/pace-loading-bar.css')

pace_barber_shop = Group([pace_barber_shop_css, pace_js])
pace_center_atom = Group([pace_center_atom_css, pace_js])
pace_center_simple = Group([pace_center_simple_css, pace_js])
pace_flash = Group([pace_flash_css, pace_js])
pace_macosx = Group([pace_macosx_css, pace_js])
pace_big_counter = Group([pace_big_counter_css, pace_js])
pace_center_circle = Group([pace_center_circle_css, pace_js])
pace_corner_indicator = Group([pace_corner_indicator_css, pace_js])
pace_flat_top = Group([pace_flat_top_css, pace_js])
pace_minimal = Group([pace_minimal_css, pace_js])
pace_bounce = Group([pace_bounce_css, pace_js])
pace_center_radar = Group([pace_center_radar_css, pace_js])
pace_fill_left = Group([pace_fill_left_css, pace_js])
pace_loading_bar = Group([pace_loading_bar_css, pace_js])

pace = pace_minimal