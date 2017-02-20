var webpack = require("webpack");
var path = require("path");

const nodeEnv = process.env.NODE_ENV || 'development';
const isProd = nodeEnv === 'production';

const VENDOR = [
    'axios',
    'lodash',
    'react',
    'react-router',
    'react-dom',
    'redux-form',
    'redux-promise'
];

const plugins = [
    new webpack.DefinePlugin({
	'process.env': { NODE_ENV: JSON.stringify(nodeEnv) }
    }),
    new webpack.NamedModulesPlugin(),
]

if (isProd) {
  plugins.push(
    new webpack.LoaderOptionsPlugin({
      minimize: true,
      debug: false
    }),
    new webpack.optimize.UglifyJsPlugin({
      compress: {
        warnings: false,
        screw_ie8: true,
        conditionals: true,
        unused: true,
        comparisons: true,
        sequences: true,
        dead_code: true,
        evaluate: true,
        if_return: true,
        join_vars: true,
      },
      output: {
        comments: false
      },
    })
  );
} else {
  plugins.push(
    new webpack.HotModuleReplacementPlugin()
  );
}

module.exports = {
    entry: {
	app: "./js/index.jsx",
	vendor : VENDOR
    },
    output: {
	publicPath: __dirname,
	path: __dirname,
	filename: "dist/bundle/[name].bundle.js"
    },
    module: {
	rules: [
	    {
		test: /\.jsx?$/,
		loader: 'eslint-loader?{fix: true}',
		exclude: /node_modules/,
		enforce: 'pre'
	    },
	    {
		use: 'babel-loader',
		test: /\.(js|jsx)$/,
		exclude: '/node_modules/'
	    }
	]
    },
    devtool: "source-map",
    devServer: {
	contentBase: './'
    },
    resolve: {
	extensions: ['.js', '.jsx'],
    },
    plugins: [
        new webpack.optimize.UglifyJsPlugin()
    ]
}
