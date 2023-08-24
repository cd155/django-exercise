{ pkgs ? import <nixpkgs> {} }:
let
  my-python-packages = ps: with ps; [
    django
    djangorestframework
    django-debug-toolbar
    bleach
    # other python packages

    ## Install package not available in Nixpkgs

    # package 1
    (
      buildPythonPackage rec {
        pname = "djangorestframework-xml";
        version = "2.0.0";
        src = fetchPypi {
          inherit pname version;
          sha256 = "35f6c811d0ab8c8466b26db234e16a2ed32d76381715257aebf4c7be2c202ca1";
        };
        doCheck = false;
        propagatedBuildInputs = [
          # Specify dependencies
          pkgs.python3Packages.defusedxml
        ];
      }
    )
    # package2 
    # djoser is not available in NixOS
    # It is not working in custom installation 
    # try to use `python -m venv .venv`
  ];
  my-python = pkgs.python3.withPackages my-python-packages;
in my-python.env