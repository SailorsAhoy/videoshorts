{ pkgs }: {
  deps = [
    pkgs.python311Full
    pkgs.python311Packages.pandas
    pkgs.python311Packages.requests
    pkgs.python311Packages.tqdm
  ];
}
