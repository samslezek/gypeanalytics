btoa = require('Base64').btoa;
$.ajax
({
  type: "GET",
  url: "https://api.mysportsfeeds.com/v1.1/pull/nba/2017-2018-regular/cumulative_player_stats.json?playerstats=2PA,2PM,3PA,3PM,FTA,FTM",
  dataType: 'json',
  async: false,
  headers: {
    "Authorization": "Basic " + btoa({email} + ":" + {password})
  },
  data: '{ "comment" }',
  success: function (){
    alert('Thanks for your comment!'); 
  }
}); 