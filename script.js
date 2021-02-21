// barChart is a JSON specification object we will use to create our visualization. All the information
// about creating it is in this single object.

var barChart = {
  height: {step: 20},

  width: 600,

  // The data key is where you declare the dataset you're using to construct the graph. You can declare it
  // manually with a list of values, or you can import in an external dataset with the url key.
  data: {
    values: [
      {"name": "We're The Lucky Ones", "popularity": 45}, {"name": "bop it up!", "popularity": 51},
      {"name": "Care For You", "popularity": 57}, {"name": "Jupiter", "popularity": 54},
      {"name": "Hold It Together", "popularity": 57}, {"name": "Out for the Night - Live", "popularity": 46},
      {"name": "...baby one more time", "popularity": 61}, {"name": "Drip", "popularity": 48},
      {"name": "Ruthless", "popularity": 60}, {"name": "Carino", "popularity": 45},
      {"name": "ABQ", "popularity": 50}, {"name": "Loverboy", "popularity": 48},
      {"name": "Over the Moon", "popularity": 60}, {"name": "Clueless", "popularity": 43},
      {"name": "I Don't Know You", "popularity": 44}, {"name": "Basta Ya", "popularity": 54},
      {"name": "I Like It", "popularity": 49}, {"name": "Only in My Dreams", "popularity": 64},
      {"name": "Superclean", "popularity": 46}, {"name": "Dejate Llevar", "popularity": 42}
    ]
  },

  // The mark key is where you specify what type of data visualization you want to make.
  mark: "bar",

  title: "Spotify popularity of The Marias discography",

  // The encoding key is where you map the data values with visual elements. At the very least, there
  // should be one axis with at least one field.
  encoding: {
    y: {field: "name", type: "nominal", sort: "-x", },
    x: {field: "popularity", 
        type: "quantitative", 
        title: "Popularity score", 
        scale: {domain: [0, 70]}}
  }
};

// vegaEmbed specifies the DOM element in the HTML file and the visualization to replace it with.
vegaEmbed('#vis', barChart);