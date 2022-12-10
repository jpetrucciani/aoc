{ jacobi ? import
    (fetchTarball {
      name = "jacobi-2022-12-10";
      url = "https://nix.cobi.dev/x/bf249329ed4c341b4e14bb16c984d6a047b1f1fa";
      sha256 = "10hc05fcrk1pgy56r4fli2pd87ldziz6c9cwih6ws88dmc3pcdpq";
    })
    { }
}:
let
  name = "aoc";

  tools = with jacobi; {
    cli = [
      bashInteractive
      bat
      bc
      curl
      gnugrep
      gnused
      gawk
      hyperfine
      jq
      yq-go
      nixpkgs-fmt
    ];
    elixir = [
      elixir
      elixir_ls
    ];
    python = [
      (python310.withPackages (p: with p; [
        requests

        # testing
        black
        mypy
      ]))
    ];
    nim = [
      nim
    ];
    vlang = [
      vlang
    ];
    scripts = [
      (writeShellScriptBin "prospector" ''
        ${prospector}/bin/prospector $@
      '')
      (writeShellScriptBin "hyper" ''
        ${hyperfine}/bin/hyperfine --runs 1000 --shell="${bashInteractive}/bin/bash" "$@"
      '')
    ];
  };

  env = jacobi.enviro {
    inherit name tools;
    mkDerivation = true;
  };
in
env
