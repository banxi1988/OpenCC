{
  "targets": [{
    "target_name": "opencc",
    "sources": [
      "../node/opencc.cc",
    ],
    "include_dirs": [
      "../src",
      "../deps/darts-clone",
      "../deps/rapidjson-1.1",
      "<!(node -e \"require('nan')\")"
    ]
  }]
}
