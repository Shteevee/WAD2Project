function getPosition(callback) {
            var geocoder = new google.maps.Geocoder();
            var postcode = "{{ postcode }}";

            geocoder.geocode({'address': postcode}, function(results, status)
            {
              if (status == google.maps.GeocoderStatus.OK)
              {
                callback({
                  latt: results[0].geometry.location.lat(),
                  long: results[0].geometry.location.lng()
                });
              }
            });
          }

function setup_map(latitude, longitude) {
            var _position = { lat: latitude, lng: longitude};

            var mapOptions = {
              zoom: 16,
              center: _position
            }

            var map = new google.maps.Map(document.getElementById('map'), mapOptions);

            var marker = new google.maps.Marker({
              position: mapOptions.center,
              map: map
            });
          }

function go() {
            setup_map(51.5073509, -0.12775829999998223);

            document.getElementById("form").onsubmit = function() {
              getPosition(function(position){

                var text = document.getElementById("text")
                text.innerHTML = "Marker position: { Longitude: "+position.long+ ",  Latitude:"+position.latt+" }";

                setup_map(position.latt, position.long);
              });
            }
          }
