$(document).ready(function() {
	$.ajax( {async: true,
                url: '/get_map/',

		success: function(values) {

			var markers = [];
			var infos = [];

			$.each(values, function(index, value) {
                var content = '<div id="' + value.id + '" class="map-popup-content-wrapper"><div class="map-popup-content"><div class="listing-window-image-wrapper">' +
                        '<a href="' + value.url + '">' +
                            '<div class="listing-window-image" style="background-image: url(' + value.image + ');"></div>' +
                            '<div class="listing-window-content">' +
                                '<div class="info">' +
                                    '<h2>' + value.title + '</h2>' +
                                    '<h3>' + value.price + '</h3>' +
                                '</div>' +
                            '</div>' +
                        '</a>' +
                    '</div></div><i class="fa fa-close close"></i></div>' +
                    '<div class="map-marker">' + value.icon + '</div>';

				markers.push({
					latLng: value.center, 
					data: value.id,			
					options: {									
						content: content,
						offset: {
            				x: -18,
            				y: -42
          				}							
					}
				});



			});

			$('#map-google').gmap3({		
				map: {									
					options:{
						styles: [{"featureType":"landscape","stylers":[{"saturation":-100},{"lightness":60}]},{"featureType":"road.local","stylers":[{"saturation":-100},{"lightness":40},{"visibility":"on"}]},{"featureType":"transit","stylers":[{"saturation":-100},{"visibility":"simplified"}]},{"featureType":"administrative.province","stylers":[{"visibility":"off"}]},{"featureType":"water","stylers":[{"color":"#a5c4c7"},{"visibility":"on"}]},{"featureType":"road.highway","elementType":"geometry.fill","stylers":[{"color":"#f69679"},{"lightness":10}]},{"featureType":"road.highway","elementType":"geometry.stroke","stylers":[{"visibility":"off"}]},{"featureType":"poi.park","elementType":"geometry.fill","stylers":[{"color":"#b6c54c"},{"lightness":40},{"saturation":-40}]},{}],
						// center:[40.771077, -73.94],
						// center: [40.761077, -73.88],
						center: [48.922486, 24.7082023],
						scrollwheel: false,
						zoom: 14
					}
				},
				marker: {
					cluster: {
						radius: 100,
					}
				},
				overlay: {
					values: markers,
					events: {
						click: function(marker, event, context) {															
							$('.map-popup-content-wrapper').css('display', 'none');

							if ($(event[0].target).hasClass('close')) {
								$('#' + context.data).css('display', 'none');
							} else {
								$('#' + context.data).css('display', 'block');
							}
						}
					}
				}
			});


				
		}		
	});
	// Clicked #zalupa_rok_1
			// $(".events-list-content").children("h3").children("a").click(function() {
			$( "#zalupa_rok_1").click(function() {
        		
        		var select_day = $("#zalupa_rok_1").attr('value');
        		// var select_day = $(".events-list-content").children("h3").children("a").attr('value');
        		// console.log(select_day);
        		// 
        		
        		// $(".map-marker").removeClass();
        		$(".map-marker").remove();
        		$.ajax( {async: true,
                url: '/get_event_map_by_date/',
                data: {'select_day':select_day},
        		success: function(values) {

			var markers = [];
			var infos = [];

			$.each(values, function(index, value) {
                var content = '<div id="' + value.id + '" class="map-popup-content-wrapper"><div class="map-popup-content"><div class="listing-window-image-wrapper">' +
                        '<a href="' + value.url + '">' +
                            '<div class="listing-window-image" style="background-image: url(' + value.image + ');"></div>' +
                            '<div class="listing-window-content">' +
                                '<div class="info">' +
                                    '<h2>' + value.title + '</h2>' +
                                    '<h3>' + value.price + '</h3>' +
                                '</div>' +
                            '</div>' +
                        '</a>' +
                    '</div></div><i class="fa fa-close close"></i></div>' +
                    '<div class="map-marker">' + value.icon + '</div>';

				markers.push({
					latLng: value.center, 
					data: value.id,			
					options: {									
						content: content,
						offset: {
            				x: -18,
            				y: -42
          				}							
					}
				});



			});
			$('#map-google').gmap3({		
				map: {									
					options:{
						styles: [{"featureType":"landscape","stylers":[{"saturation":-100},{"lightness":60}]},{"featureType":"road.local","stylers":[{"saturation":-100},{"lightness":40},{"visibility":"on"}]},{"featureType":"transit","stylers":[{"saturation":-100},{"visibility":"simplified"}]},{"featureType":"administrative.province","stylers":[{"visibility":"off"}]},{"featureType":"water","stylers":[{"color":"#a5c4c7"},{"visibility":"on"}]},{"featureType":"road.highway","elementType":"geometry.fill","stylers":[{"color":"#f69679"},{"lightness":10}]},{"featureType":"road.highway","elementType":"geometry.stroke","stylers":[{"visibility":"off"}]},{"featureType":"poi.park","elementType":"geometry.fill","stylers":[{"color":"#b6c54c"},{"lightness":40},{"saturation":-40}]},{}],
						// center:[40.771077, -73.94],
						// center: [40.761077, -73.88],
						center: [48.922486, 24.7082023],
						scrollwheel: false,
						zoom: 14
					}
				},
				marker: {
					cluster: {
						radius: 100,
					}
				},
				overlay: {
					values: markers,
					events: {
						click: function(marker, event, context) {															
							$('.map-popup-content-wrapper').css('display', 'none');

							if ($(event[0].target).hasClass('close')) {
								$('#' + context.data).css('display', 'none');
							} else {
								$('#' + context.data).css('display', 'block');
							}
						}
					}
				}
			});


				
		}		
	});
        		
			});
			// End Ckilked	
	// Clicked #zalupa_rok_1
			// $(".events-list-content").children("h3").children("a").click(function() {
			$( "#zalupa_rok_2").click(function() {
        		
        		var select_day = $("#zalupa_rok_2").attr('value');
        		// var select_day = $(".events-list-content").children("h3").children("a").attr('value');
        		// console.log(select_day);
        		// 
        		
        		// $(".map-marker").removeClass();
        		$(".map-marker").remove();
        		$.ajax( {async: true,
                url: '/get_event_map_by_date/',
                data: {'select_day':select_day},
        		success: function(values) {

			var markers = [];
			var infos = [];

			$.each(values, function(index, value) {
                var content = '<div id="' + value.id + '" class="map-popup-content-wrapper"><div class="map-popup-content"><div class="listing-window-image-wrapper">' +
                        '<a href="' + value.url + '">' +
                            '<div class="listing-window-image" style="background-image: url(' + value.image + ');"></div>' +
                            '<div class="listing-window-content">' +
                                '<div class="info">' +
                                    '<h2>' + value.title + '</h2>' +
                                    '<h3>' + value.price + '</h3>' +
                                '</div>' +
                            '</div>' +
                        '</a>' +
                    '</div></div><i class="fa fa-close close"></i></div>' +
                    '<div class="map-marker">' + value.icon + '</div>';

				markers.push({
					latLng: value.center, 
					data: value.id,			
					options: {									
						content: content,
						offset: {
            				x: -18,
            				y: -42
          				}							
					}
				});



			});
			$('#map-google').gmap3({		
				map: {									
					options:{
						styles: [{"featureType":"landscape","stylers":[{"saturation":-100},{"lightness":60}]},{"featureType":"road.local","stylers":[{"saturation":-100},{"lightness":40},{"visibility":"on"}]},{"featureType":"transit","stylers":[{"saturation":-100},{"visibility":"simplified"}]},{"featureType":"administrative.province","stylers":[{"visibility":"off"}]},{"featureType":"water","stylers":[{"color":"#a5c4c7"},{"visibility":"on"}]},{"featureType":"road.highway","elementType":"geometry.fill","stylers":[{"color":"#f69679"},{"lightness":10}]},{"featureType":"road.highway","elementType":"geometry.stroke","stylers":[{"visibility":"off"}]},{"featureType":"poi.park","elementType":"geometry.fill","stylers":[{"color":"#b6c54c"},{"lightness":40},{"saturation":-40}]},{}],
						// center:[40.771077, -73.94],
						// center: [40.761077, -73.88],
						center: [48.922486, 24.7082023],
						scrollwheel: false,
						zoom: 14
					}
				},
				marker: {
					cluster: {
						radius: 100,
					}
				},
				overlay: {
					values: markers,
					events: {
						click: function(marker, event, context) {															
							$('.map-popup-content-wrapper').css('display', 'none');

							if ($(event[0].target).hasClass('close')) {
								$('#' + context.data).css('display', 'none');
							} else {
								$('#' + context.data).css('display', 'block');
							}
						}
					}
				}
			});


				
		}		
	});
        		
			});
			// End Ckilked	
	// Clicked #zalupa_rok_1
			// $(".events-list-content").children("h3").children("a").click(function() {
			$( "#zalupa_rok_3").click(function() {
        		
        		var select_day = $("#zalupa_rok_3").attr('value');
        		// var select_day = $(".events-list-content").children("h3").children("a").attr('value');
        		// console.log(select_day);
        		// 
        		
        		// $(".map-marker").removeClass();
        		$(".map-marker").remove();
        		$.ajax( {async: true,
                url: '/get_event_map_by_date/',
                data: {'select_day':select_day},
        		success: function(values) {

			var markers = [];
			var infos = [];

			$.each(values, function(index, value) {
                var content = '<div id="' + value.id + '" class="map-popup-content-wrapper"><div class="map-popup-content"><div class="listing-window-image-wrapper">' +
                        '<a href="' + value.url + '">' +
                            '<div class="listing-window-image" style="background-image: url(' + value.image + ');"></div>' +
                            '<div class="listing-window-content">' +
                                '<div class="info">' +
                                    '<h2>' + value.title + '</h2>' +
                                    '<h3>' + value.price + '</h3>' +
                                '</div>' +
                            '</div>' +
                        '</a>' +
                    '</div></div><i class="fa fa-close close"></i></div>' +
                    '<div class="map-marker">' + value.icon + '</div>';

				markers.push({
					latLng: value.center, 
					data: value.id,			
					options: {									
						content: content,
						offset: {
            				x: -18,
            				y: -42
          				}							
					}
				});



			});
			$('#map-google').gmap3({		
				map: {									
					options:{
						styles: [{"featureType":"landscape","stylers":[{"saturation":-100},{"lightness":60}]},{"featureType":"road.local","stylers":[{"saturation":-100},{"lightness":40},{"visibility":"on"}]},{"featureType":"transit","stylers":[{"saturation":-100},{"visibility":"simplified"}]},{"featureType":"administrative.province","stylers":[{"visibility":"off"}]},{"featureType":"water","stylers":[{"color":"#a5c4c7"},{"visibility":"on"}]},{"featureType":"road.highway","elementType":"geometry.fill","stylers":[{"color":"#f69679"},{"lightness":10}]},{"featureType":"road.highway","elementType":"geometry.stroke","stylers":[{"visibility":"off"}]},{"featureType":"poi.park","elementType":"geometry.fill","stylers":[{"color":"#b6c54c"},{"lightness":40},{"saturation":-40}]},{}],
						// center:[40.771077, -73.94],
						// center: [40.761077, -73.88],
						center: [48.922486, 24.7082023],
						scrollwheel: false,
						zoom: 14
					}
				},
				marker: {
					cluster: {
						radius: 100,
					}
				},
				overlay: {
					values: markers,
					events: {
						click: function(marker, event, context) {															
							$('.map-popup-content-wrapper').css('display', 'none');

							if ($(event[0].target).hasClass('close')) {
								$('#' + context.data).css('display', 'none');
							} else {
								$('#' + context.data).css('display', 'block');
							}
						}
					}
				}
			});


				
		}		
	});
        		
			});
			// End Ckilked	
	// Clicked #zalupa_rok_1
			// $(".events-list-content").children("h3").children("a").click(function() {
			$( "#zalupa_rok_4").click(function() {
        		
        		var select_day = $("#zalupa_rok_4").attr('value');
        		// var select_day = $(".events-list-content").children("h3").children("a").attr('value');
        		// console.log(select_day);
        		// 
        		
        		// $(".map-marker").removeClass();
        		$(".map-marker").remove();
        		$.ajax( {async: true,
                url: '/get_event_map_by_date/',
                data: {'select_day':select_day},
        		success: function(values) {

			var markers = [];
			var infos = [];

			$.each(values, function(index, value) {
                var content = '<div id="' + value.id + '" class="map-popup-content-wrapper"><div class="map-popup-content"><div class="listing-window-image-wrapper">' +
                        '<a href="' + value.url + '">' +
                            '<div class="listing-window-image" style="background-image: url(' + value.image + ');"></div>' +
                            '<div class="listing-window-content">' +
                                '<div class="info">' +
                                    '<h2>' + value.title + '</h2>' +
                                    '<h3>' + value.price + '</h3>' +
                                '</div>' +
                            '</div>' +
                        '</a>' +
                    '</div></div><i class="fa fa-close close"></i></div>' +
                    '<div class="map-marker">' + value.icon + '</div>';

				markers.push({
					latLng: value.center, 
					data: value.id,			
					options: {									
						content: content,
						offset: {
            				x: -18,
            				y: -42
          				}							
					}
				});



			});
			$('#map-google').gmap3({		
				map: {									
					options:{
						styles: [{"featureType":"landscape","stylers":[{"saturation":-100},{"lightness":60}]},{"featureType":"road.local","stylers":[{"saturation":-100},{"lightness":40},{"visibility":"on"}]},{"featureType":"transit","stylers":[{"saturation":-100},{"visibility":"simplified"}]},{"featureType":"administrative.province","stylers":[{"visibility":"off"}]},{"featureType":"water","stylers":[{"color":"#a5c4c7"},{"visibility":"on"}]},{"featureType":"road.highway","elementType":"geometry.fill","stylers":[{"color":"#f69679"},{"lightness":10}]},{"featureType":"road.highway","elementType":"geometry.stroke","stylers":[{"visibility":"off"}]},{"featureType":"poi.park","elementType":"geometry.fill","stylers":[{"color":"#b6c54c"},{"lightness":40},{"saturation":-40}]},{}],
						// center:[40.771077, -73.94],
						// center: [40.761077, -73.88],
						center: [48.922486, 24.7082023],
						scrollwheel: false,
						zoom: 14
					}
				},
				marker: {
					cluster: {
						radius: 100,
					}
				},
				overlay: {
					values: markers,
					events: {
						click: function(marker, event, context) {															
							$('.map-popup-content-wrapper').css('display', 'none');

							if ($(event[0].target).hasClass('close')) {
								$('#' + context.data).css('display', 'none');
							} else {
								$('#' + context.data).css('display', 'block');
							}
						}
					}
				}
			});


				
		}		
	});
        		
			});
			// End Ckilked	
	// Clicked #zalupa_rok_5
			// $(".events-list-content").children("h3").children("a").click(function() {
			$( "#zalupa_rok_5").click(function() {
        		
        		var select_day = $("#zalupa_rok_5").attr('value');
        		// var select_day = $(".events-list-content").children("h3").children("a").attr('value');
        		// console.log(select_day);
        		// 
        		
        		// $(".map-marker").removeClass();
        		$(".map-marker").remove();
        		$.ajax( {async: true,
                url: '/get_event_map_by_date/',
                data: {'select_day':select_day},
        		success: function(values) {

			var markers = [];
			var infos = [];

			$.each(values, function(index, value) {
                var content = '<div id="' + value.id + '" class="map-popup-content-wrapper"><div class="map-popup-content"><div class="listing-window-image-wrapper">' +
                        '<a href="' + value.url + '">' +
                            '<div class="listing-window-image" style="background-image: url(' + value.image + ');"></div>' +
                            '<div class="listing-window-content">' +
                                '<div class="info">' +
                                    '<h2>' + value.title + '</h2>' +
                                    '<h3>' + value.price + '</h3>' +
                                '</div>' +
                            '</div>' +
                        '</a>' +
                    '</div></div><i class="fa fa-close close"></i></div>' +
                    '<div class="map-marker">' + value.icon + '</div>';

				markers.push({
					latLng: value.center, 
					data: value.id,			
					options: {									
						content: content,
						offset: {
            				x: -18,
            				y: -42
          				}							
					}
				});



			});
			$('#map-google').gmap3({		
				map: {									
					options:{
						styles: [{"featureType":"landscape","stylers":[{"saturation":-100},{"lightness":60}]},{"featureType":"road.local","stylers":[{"saturation":-100},{"lightness":40},{"visibility":"on"}]},{"featureType":"transit","stylers":[{"saturation":-100},{"visibility":"simplified"}]},{"featureType":"administrative.province","stylers":[{"visibility":"off"}]},{"featureType":"water","stylers":[{"color":"#a5c4c7"},{"visibility":"on"}]},{"featureType":"road.highway","elementType":"geometry.fill","stylers":[{"color":"#f69679"},{"lightness":10}]},{"featureType":"road.highway","elementType":"geometry.stroke","stylers":[{"visibility":"off"}]},{"featureType":"poi.park","elementType":"geometry.fill","stylers":[{"color":"#b6c54c"},{"lightness":40},{"saturation":-40}]},{}],
						// center:[40.771077, -73.94],
						// center: [40.761077, -73.88],
						center: [48.922486, 24.7082023],
						scrollwheel: false,
						zoom: 14
					}
				},
				marker: {
					cluster: {
						radius: 100,
					}
				},
				overlay: {
					values: markers,
					events: {
						click: function(marker, event, context) {															
							$('.map-popup-content-wrapper').css('display', 'none');

							if ($(event[0].target).hasClass('close')) {
								$('#' + context.data).css('display', 'none');
							} else {
								$('#' + context.data).css('display', 'block');
							}
						}
					}
				}
			});


				
		}		
	});
        		
			});
			// End Ckilked	
	// Clicked #zalupa_rok_6
			// $(".events-list-content").children("h3").children("a").click(function() {
			$( "#zalupa_rok_6").click(function() {
        		
        		var select_day = $("#zalupa_rok_6").attr('value');
        		// var select_day = $(".events-list-content").children("h3").children("a").attr('value');
        		// console.log(select_day);
        		// 
        		
        		// $(".map-marker").removeClass();
        		$(".map-marker").remove();
        		$.ajax( {async: true,
                url: '/get_event_map_by_date/',
                data: {'select_day':select_day},
        		success: function(values) {

			var markers = [];
			var infos = [];

			$.each(values, function(index, value) {
                var content = '<div id="' + value.id + '" class="map-popup-content-wrapper"><div class="map-popup-content"><div class="listing-window-image-wrapper">' +
                        '<a href="' + value.url + '">' +
                            '<div class="listing-window-image" style="background-image: url(' + value.image + ');"></div>' +
                            '<div class="listing-window-content">' +
                                '<div class="info">' +
                                    '<h2>' + value.title + '</h2>' +
                                    '<h3>' + value.price + '</h3>' +
                                '</div>' +
                            '</div>' +
                        '</a>' +
                    '</div></div><i class="fa fa-close close"></i></div>' +
                    '<div class="map-marker">' + value.icon + '</div>';

				markers.push({
					latLng: value.center, 
					data: value.id,			
					options: {									
						content: content,
						offset: {
            				x: -18,
            				y: -42
          				}							
					}
				});



			});
			$('#map-google').gmap3({		
				map: {									
					options:{
						styles: [{"featureType":"landscape","stylers":[{"saturation":-100},{"lightness":60}]},{"featureType":"road.local","stylers":[{"saturation":-100},{"lightness":40},{"visibility":"on"}]},{"featureType":"transit","stylers":[{"saturation":-100},{"visibility":"simplified"}]},{"featureType":"administrative.province","stylers":[{"visibility":"off"}]},{"featureType":"water","stylers":[{"color":"#a5c4c7"},{"visibility":"on"}]},{"featureType":"road.highway","elementType":"geometry.fill","stylers":[{"color":"#f69679"},{"lightness":10}]},{"featureType":"road.highway","elementType":"geometry.stroke","stylers":[{"visibility":"off"}]},{"featureType":"poi.park","elementType":"geometry.fill","stylers":[{"color":"#b6c54c"},{"lightness":40},{"saturation":-40}]},{}],
						// center:[40.771077, -73.94],
						// center: [40.761077, -73.88],
						center: [48.922486, 24.7082023],
						scrollwheel: false,
						zoom: 14
					}
				},
				marker: {
					cluster: {
						radius: 100,
					}
				},
				overlay: {
					values: markers,
					events: {
						click: function(marker, event, context) {															
							$('.map-popup-content-wrapper').css('display', 'none');

							if ($(event[0].target).hasClass('close')) {
								$('#' + context.data).css('display', 'none');
							} else {
								$('#' + context.data).css('display', 'block');
							}
						}
					}
				}
			});


				
		}		
	});
        		
			});
			// End Ckilked	
	// Clicked #zalupa_rok_7
			// $(".events-list-content").children("h3").children("a").click(function() {
			$( "#zalupa_rok_7").click(function() {
        		
        		var select_day = $("#zalupa_rok_7").attr('value');
        		// var select_day = $(".events-list-content").children("h3").children("a").attr('value');
        		// console.log(select_day);
        		// 
        		
        		// $(".map-marker").removeClass();
        		$(".map-marker").remove();
        		$.ajax( {async: true,
                url: '/get_event_map_by_date/',
                data: {'select_day':select_day},
        		success: function(values) {

			var markers = [];
			var infos = [];

			$.each(values, function(index, value) {
                var content = '<div id="' + value.id + '" class="map-popup-content-wrapper"><div class="map-popup-content"><div class="listing-window-image-wrapper">' +
                        '<a href="' + value.url + '">' +
                            '<div class="listing-window-image" style="background-image: url(' + value.image + ');"></div>' +
                            '<div class="listing-window-content">' +
                                '<div class="info">' +
                                    '<h2>' + value.title + '</h2>' +
                                    '<h3>' + value.price + '</h3>' +
                                '</div>' +
                            '</div>' +
                        '</a>' +
                    '</div></div><i class="fa fa-close close"></i></div>' +
                    '<div class="map-marker">' + value.icon + '</div>';

				markers.push({
					latLng: value.center, 
					data: value.id,			
					options: {									
						content: content,
						offset: {
            				x: -18,
            				y: -42
          				}							
					}
				});



			});
			$('#map-google').gmap3({		
				map: {									
					options:{
						styles: [{"featureType":"landscape","stylers":[{"saturation":-100},{"lightness":60}]},{"featureType":"road.local","stylers":[{"saturation":-100},{"lightness":40},{"visibility":"on"}]},{"featureType":"transit","stylers":[{"saturation":-100},{"visibility":"simplified"}]},{"featureType":"administrative.province","stylers":[{"visibility":"off"}]},{"featureType":"water","stylers":[{"color":"#a5c4c7"},{"visibility":"on"}]},{"featureType":"road.highway","elementType":"geometry.fill","stylers":[{"color":"#f69679"},{"lightness":10}]},{"featureType":"road.highway","elementType":"geometry.stroke","stylers":[{"visibility":"off"}]},{"featureType":"poi.park","elementType":"geometry.fill","stylers":[{"color":"#b6c54c"},{"lightness":40},{"saturation":-40}]},{}],
						// center:[40.771077, -73.94],
						// center: [40.761077, -73.88],
						center: [48.922486, 24.7082023],
						scrollwheel: false,
						zoom: 14
					}
				},
				marker: {
					cluster: {
						radius: 100,
					}
				},
				overlay: {
					values: markers,
					events: {
						click: function(marker, event, context) {															
							$('.map-popup-content-wrapper').css('display', 'none');

							if ($(event[0].target).hasClass('close')) {
								$('#' + context.data).css('display', 'none');
							} else {
								$('#' + context.data).css('display', 'block');
							}
						}
					}
				}
			});


				
		}		
	});
        		
			});
			// End Ckilked	
});