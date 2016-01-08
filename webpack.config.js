module.exports = {
  context: __dirname + "/app",
  entry: {
    javascript: "./app.js",
    html: "./index.html",
  },

  output: {
    filename: "app.js",
    path: __dirname + "/dist",
  },

  module: {
    loaders: [
      {
        test: /\.jsx?$/,
        exclude: /(node_modules|bower_components)/,
        loader: "babel",
        query: {
          presets: ["react", "es2015"]
        }
      },
      {
        test: /\.scss$/,
        loaders: ["style", "css", "sass?sourceMap"]
      },
      {
        test: /\.html$/,
        loader: "file?name=[name].[ext]",
      },
      {
        test: /\.(png|jpg)$/,
        loader: "url?limit=25000"
      }
    ],
  }
}