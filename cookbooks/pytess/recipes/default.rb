#
# Cookbook Name:: pytess
# Recipe:: default
#

apt_package "git-core" do
  action :install
end

apt_package "language-pack-en" do
  action :install
end

apt_package "python-pip" do
  action :install
end

apt_package "tesseract-ocr" do
  action :install
end

apt_package "python-imaging" do
  action :install
end

apt_package "poppler-utils" do
  action :install
end
