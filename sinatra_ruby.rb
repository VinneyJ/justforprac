require 'rubygems'
require 'sinatra'


get '/' do
    "THis is the home page"
end

get '/about' do
    "This is the about page"
end

get '/contact' do
    "This is our contact page"
end