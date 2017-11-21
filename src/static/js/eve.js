$(document).ready(function() {
	'use strict';
		// Photo chooser
		function readURL(input) {

		    if (input.files && input.files[0]) {
		        var reader = new FileReader();

		        reader.onload = function (e) {
		        	console.log(e.target.result)
		            $('#photoXXX-photo').css('background-image', 'url(' + e.target.result + ')');
		        }

		        reader.readAsDataURL(input.files[0]);
		    }
		}
		$('#photoXXX').on('change', function() {
			readURL(this)
		});
	    /*================== Date Picker Initialization ===================*/
        $('#input_dateinput').pickadate({
        	format: 'dd/mm/yyyy',
        	today: '',
			clear: '',
			close: ''
        });

        $('#event_time').pickatime({
        	format: 'hh:i'
        });
    /**
     * Scroll
     */
    $(window).scroll(function() {
        if ($(this).scrollTop() > 220) {
            $('.header-sticky').addClass('active');
        } else {
            $('.header-sticky').removeClass('active');
        }
    });

    /**
     * Filter
     */
	$('.filter h2').on('click', function(e) {
		$(this).toggleClass('closed');
	});

    /**
     * Checkbox & radio inputs
     */
    $('input[type=checkbox], input[type=radio]').ezMark();

	/**
	 * Sidenav trigger
	 */
	$('.sidenav-trigger, .sidenav-close, .page-wrapper-overlay').on('click', function(e) {
		e.preventDefault();
		$('body').toggleClass('sidenav-open');
	});
	
	/** 
	 * Hero Video
	 */	
	jQuery("#hero-video").YTPlayer();

	/**
	 * Cover carousel
	 */
	 $('.event-gallery').owlCarousel({
	 	autoplay: false,
	 	loop: true,
	 	items: 4,	 	
	 	nav: true,
	 	navText: ['<i class="entypo-chevron-with-circle-left"></i>', '<i class="entypo-chevron-with-circle-right"></i>']
	 });

	/**
	 * Animations
	 */
	$('body').addClass('loaded');

	/**
	 * Autocomplete
	 */
	// $.get('assets/data/autocomplete.json', function(data){
	$.get('/static/data/autocomplete.json', function(data){
    	$('.header-search input').typeahead({ 
    		source: data,
		    select: function () {
		      var val = this.$menu.find('.active').data('value');
		      this.$element.data('active', val);
		      if(this.autoSelect || val) {
		        var newVal = this.updater(val);

		        if (!newVal) {
		          newVal = "";
		        }

		        this.$element
		          .val(newVal.name)
		          .change();
		        this.afterSelect(newVal);
		      }
		      return this.hide();
		    },	         		
    		displayText: function(item) {
    			return '<img src="' + item.image + '"><strong>' + item.name + '</strong><span>' + item.category + '</span>';
    		},
			highlighter: function(item) { 
				return unescape(item);				
			},		
    		autoSelect: true
    	});
	}, 'json');

	/**
	 * Google Map
	 */
	var markers = [];
	



	$('#contact-map').gmap3({
		map: {									
			options:{
				styles: [{"featureType":"water","elementType":"geometry","stylers":[{"color":"#e9e9e9"},{"lightness":17}]},{"featureType":"landscape","elementType":"geometry","stylers":[{"color":"#f5f5f5"},{"lightness":20}]},{"featureType":"road.highway","elementType":"geometry.fill","stylers":[{"color":"#ffffff"},{"lightness":17}]},{"featureType":"road.highway","elementType":"geometry.stroke","stylers":[{"color":"#ffffff"},{"lightness":29},{"weight":0.2}]},{"featureType":"road.arterial","elementType":"geometry","stylers":[{"color":"#ffffff"},{"lightness":18}]},{"featureType":"road.local","elementType":"geometry","stylers":[{"color":"#ffffff"},{"lightness":16}]},{"featureType":"poi","elementType":"geometry","stylers":[{"color":"#f5f5f5"},{"lightness":21}]},{"featureType":"poi.park","elementType":"geometry","stylers":[{"color":"#dedede"},{"lightness":21}]},{"elementType":"labels.text.stroke","stylers":[{"visibility":"on"},{"color":"#ffffff"},{"lightness":16}]},{"elementType":"labels.text.fill","stylers":[{"saturation":36},{"color":"#333333"},{"lightness":40}]},{"elementType":"labels.icon","stylers":[{"visibility":"off"}]},{"featureType":"transit","elementType":"geometry","stylers":[{"color":"#f2f2f2"},{"lightness":19}]},{"featureType":"administrative","elementType":"geometry.fill","stylers":[{"color":"#fefefe"},{"lightness":20}]},{"featureType":"administrative","elementType":"geometry.stroke","stylers":[{"color":"#fefefe"},{"lightness":17},{"weight":1.2}]}],
				// center: [40.761077, -73.88],
				center: [48.922486, 24.7082023],
				scrollwheel: false,
				zoom: 12
			},
		},
		marker: {
			cluster: {
				radius: 100,
			}
		},			
		overlay: {
			values: [{
				// latLng: [40.761077, -73.88], 
				latLng: [48.922486, 24.7082023],
				data: 1,			
				options: {									
					content: '<div class="map-marker"><i class="fa fa-star"></i></div>', 
					offset: {
        				x: -18,
        				y: -42
      				}							
				}									
			}],
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
	    //  	$.ajax({
     //            async: true,
     //            url: 'get_map/',
	    //         // data: {'select_rooms':select_rooms},
     //            success: function(values) {
     //            	// console.log(values);
     //            	var markers = [];
					// var infos = [];

     //            },
     //            // dataType: 'json',
     //        });
			

	/**
	 * Customizer
	 */	 
	$('.customizer-title').on('click', function() {		
		$('.customizer').toggleClass('open');
	});

	$('.customizer a').click('click', function(e) {
		e.preventDefault();

		var cssFile = $(this).attr('href');
		$('#css-primary').attr('href', cssFile);
	});		
});