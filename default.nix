{ jacobi ? import
    (fetchTarball {
      name = "jacobi-2022-12-01";
      url = "https://nix.cobi.dev/x/15e5cfd7927420eddc8d822e2dc0ee32908c850b";
      sha256 = "139k9dnqb5k1n7r1i6hk7vfiy9nmmla4hdvczi14sa4lv7grg7aq";
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
      jq
      yq-go
      nixpkgs-fmt
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
    ];
  };

  env = jacobi.enviro {
    inherit name tools;
    mkDerivation = true;
  };
in
env
