## macOS

1. make 需要 `Doxygen` (可以通过 brew 安装)

```
➜  OpenCC (master) ✔ make PREFIX=/usr/local
mkdir -p build/rel
(cd build/rel; cmake \
	-DBUILD_DOCUMENTATION:BOOL=ON \
	-DENABLE_GTEST:BOOL=OFF \
	-DCMAKE_BUILD_TYPE=Release \
	-DCMAKE_INSTALL_PREFIX=/usr/local \
	../..)
-- The CXX compiler identification is AppleClang 10.0.0.10001145
-- Check for working CXX compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++
-- Check for working CXX compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Performing Test COMPILER_HAS_HIDDEN_VISIBILITY
-- Performing Test COMPILER_HAS_HIDDEN_VISIBILITY - Success
-- Performing Test COMPILER_HAS_HIDDEN_INLINE_VISIBILITY
-- Performing Test COMPILER_HAS_HIDDEN_INLINE_VISIBILITY - Success
-- Performing Test COMPILER_HAS_DEPRECATED_ATTR
-- Performing Test COMPILER_HAS_DEPRECATED_ATTR - Success
-- Could NOT find Doxygen (missing:  DOXYGEN_EXECUTABLE)
CMake Error at doc/CMakeLists.txt:4 (message):
  Doxygen is needed to build the documentation.  Please install it correctly


-- Configuring incomplete, errors occurred!
See also "/Users/banxi/Workspace/OpenCC/build/rel/CMakeFiles/CMakeOutput.log".
make: *** [build] Error 1
```

安装好 doxygen 之后可以编译成功。

```
➜  OpenCC (master) ✗ make PREFIX=/usr/local
mkdir -p build/rel
(cd build/rel; cmake \
	-DBUILD_DOCUMENTATION:BOOL=ON \
	-DENABLE_GTEST:BOOL=OFF \
	-DCMAKE_BUILD_TYPE=Release \
	-DCMAKE_INSTALL_PREFIX=/usr/local \
	../..)
-- Found Doxygen: /usr/local/bin/doxygen (found version "1.8.14")
-- Configuring done
-- Generating done
-- Build files have been written to: /Users/banxi/Workspace/OpenCC/build/rel
make -C build/rel VERBOSE= PREFIX=/usr/local
Dependee "/Users/banxi/Workspace/OpenCC/build/rel/src/CMakeFiles/libopencc.dir/DependInfo.cmake" is newer than depender "/Users/banxi/Workspace/OpenCC/build/rel/src/CMakeFiles/libopencc.dir/depend.internal".
Dependee "/Users/banxi/Workspace/OpenCC/build/rel/src/CMakeFiles/CMakeDirectoryInformation.cmake" is newer than depender "/Users/banxi/Workspace/OpenCC/build/rel/src/CMakeFiles/libopencc.dir/depend.internal".
Scanning dependencies of target libopencc
[  2%] Building CXX object src/CMakeFiles/libopencc.dir/BinaryDict.cpp.o
[  4%] Building CXX object src/CMakeFiles/libopencc.dir/Config.cpp.o
[  6%] Building CXX object src/CMakeFiles/libopencc.dir/Conversion.cpp.o
[  9%] Building CXX object src/CMakeFiles/libopencc.dir/ConversionChain.cpp.o
[ 11%] Building CXX object src/CMakeFiles/libopencc.dir/Converter.cpp.o
[ 13%] Building CXX object src/CMakeFiles/libopencc.dir/DartsDict.cpp.o
[ 16%] Building CXX object src/CMakeFiles/libopencc.dir/Dict.cpp.o
[ 18%] Building CXX object src/CMakeFiles/libopencc.dir/DictConverter.cpp.o
[ 20%] Building CXX object src/CMakeFiles/libopencc.dir/DictEntry.cpp.o
[ 23%] Building CXX object src/CMakeFiles/libopencc.dir/DictGroup.cpp.o
[ 25%] Building CXX object src/CMakeFiles/libopencc.dir/MaxMatchSegmentation.cpp.o
[ 27%] Building CXX object src/CMakeFiles/libopencc.dir/PhraseExtract.cpp.o
[ 30%] Building CXX object src/CMakeFiles/libopencc.dir/SimpleConverter.cpp.o
[ 32%] Building CXX object src/CMakeFiles/libopencc.dir/Segmentation.cpp.o
[ 34%] Building CXX object src/CMakeFiles/libopencc.dir/TextDict.cpp.o
[ 37%] Building CXX object src/CMakeFiles/libopencc.dir/UTF8StringSlice.cpp.o
[ 39%] Building CXX object src/CMakeFiles/libopencc.dir/UTF8Util.cpp.o
[ 41%] Linking CXX shared library libopencc.dylib
[ 41%] Built target libopencc
Dependee "/Users/banxi/Workspace/OpenCC/build/rel/src/tools/CMakeFiles/opencc_phrase_extract.dir/DependInfo.cmake" is newer than depender "/Users/banxi/Workspace/OpenCC/build/rel/src/tools/CMakeFiles/opencc_phrase_extract.dir/depend.internal".
Dependee "/Users/banxi/Workspace/OpenCC/build/rel/src/tools/CMakeFiles/CMakeDirectoryInformation.cmake" is newer than depender "/Users/banxi/Workspace/OpenCC/build/rel/src/tools/CMakeFiles/opencc_phrase_extract.dir/depend.internal".
Scanning dependencies of target opencc_phrase_extract
[ 44%] Building CXX object src/tools/CMakeFiles/opencc_phrase_extract.dir/PhraseExtract.cpp.o
[ 46%] Linking CXX executable opencc_phrase_extract
[ 46%] Built target opencc_phrase_extract
Dependee "/Users/banxi/Workspace/OpenCC/build/rel/src/tools/CMakeFiles/opencc_dict.dir/DependInfo.cmake" is newer than depender "/Users/banxi/Workspace/OpenCC/build/rel/src/tools/CMakeFiles/opencc_dict.dir/depend.internal".
Dependee "/Users/banxi/Workspace/OpenCC/build/rel/src/tools/CMakeFiles/CMakeDirectoryInformation.cmake" is newer than depender "/Users/banxi/Workspace/OpenCC/build/rel/src/tools/CMakeFiles/opencc_dict.dir/depend.internal".
Scanning dependencies of target opencc_dict
[ 48%] Building CXX object src/tools/CMakeFiles/opencc_dict.dir/DictConverter.cpp.o
[ 51%] Linking CXX executable opencc_dict
[ 51%] Built target opencc_dict
Dependee "/Users/banxi/Workspace/OpenCC/build/rel/src/tools/CMakeFiles/opencc.dir/DependInfo.cmake" is newer than depender "/Users/banxi/Workspace/OpenCC/build/rel/src/tools/CMakeFiles/opencc.dir/depend.internal".
Dependee "/Users/banxi/Workspace/OpenCC/build/rel/src/tools/CMakeFiles/CMakeDirectoryInformation.cmake" is newer than depender "/Users/banxi/Workspace/OpenCC/build/rel/src/tools/CMakeFiles/opencc.dir/depend.internal".
Scanning dependencies of target opencc
[ 53%] Building CXX object src/tools/CMakeFiles/opencc.dir/CommandLine.cpp.o
/Users/banxi/Workspace/OpenCC/src/tools/CommandLine.cpp:87:38: warning: 'tmpnam' is deprecated: This function is
      provided for compatibility reasons only. Due to security concerns inherent in the design of tmpnam(3), it is
      highly recommended that you use mkstemp(3) instead. [-Wdeprecated-declarations]
    const string tempFileName = std::tmpnam(nullptr);
                                     ^
/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.14.sdk/usr/include/stdio.h:186:1: note:
      'tmpnam' has been explicitly marked deprecated here
__deprecated_msg("This function is provided for compatibility reasons only.  Due to security concerns inher...
^
/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.14.sdk/usr/include/sys/cdefs.h:180:48: note:
      expanded from macro '__deprecated_msg'
        #define __deprecated_msg(_msg) __attribute__((deprecated(_msg)))
                                                      ^
1 warning generated.
[ 55%] Linking CXX executable opencc
[ 55%] Built target opencc
Dependee "/Users/banxi/Workspace/OpenCC/build/rel/doc/CMakeFiles/apidoc.dir/DependInfo.cmake" is newer than depender "/Users/banxi/Workspace/OpenCC/build/rel/doc/CMakeFiles/apidoc.dir/depend.internal".
Dependee "/Users/banxi/Workspace/OpenCC/build/rel/doc/CMakeFiles/CMakeDirectoryInformation.cmake" is newer than depender "/Users/banxi/Workspace/OpenCC/build/rel/doc/CMakeFiles/apidoc.dir/depend.internal".
Scanning dependencies of target apidoc
[ 58%] Building API Documentation
/Users/banxi/Workspace/OpenCC/README.md:3: warning: Unexpected html tag <img> found within <a href=...> context
/Users/banxi/Workspace/OpenCC/README.md:4: warning: Unexpected html tag <img> found within <a href=...> context
/Users/banxi/Workspace/OpenCC/README.md:5: warning: Unexpected html tag <img> found within <a href=...> context
[ 58%] Built target apidoc
Dependee "/Users/banxi/Workspace/OpenCC/build/rel/data/CMakeFiles/Dictionaries.dir/DependInfo.cmake" is newer than depender "/Users/banxi/Workspace/OpenCC/build/rel/data/CMakeFiles/Dictionaries.dir/depend.internal".
Dependee "/Users/banxi/Workspace/OpenCC/build/rel/data/CMakeFiles/CMakeDirectoryInformation.cmake" is newer than depender "/Users/banxi/Workspace/OpenCC/build/rel/data/CMakeFiles/Dictionaries.dir/depend.internal".
Scanning dependencies of target Dictionaries
[ 60%] Building STCharacters.ocd
[ 62%] Building STPhrases.ocd
[ 65%] Building TSCharacters.ocd
[ 67%] Building TSPhrases.ocd
[ 69%] Building TWVariants.ocd
[ 72%] Building TWVariantsRevPhrases.ocd
[ 74%] Building JPVariants.ocd
[ 76%] Building HKVariants.ocd
[ 79%] Building HKVariantsPhrases.ocd
[ 81%] Building HKVariantsRevPhrases.ocd
[ 83%] Generating TWPhrases.txt
[ 86%] Building TWPhrases.ocd
[ 88%] Generating TWPhrasesRev.txt
[ 90%] Building TWPhrasesRev.ocd
[ 93%] Generating TWVariantsRev.txt
[ 95%] Building TWVariantsRev.ocd
[ 97%] Generating HKVariantsRev.txt
[100%] Building HKVariantsRev.ocd
[100%] Built target Dictionaries
```

2. 使用 yarn 初始化项目

```
➜  OpenCC (master) ✗ yarn
yarn install v1.10.1
info No lockfile found.
[1/4] 🔍  Resolving packages...
warning node-pre-gyp > hawk > hoek@2.16.3: The major version is no longer supported. Please update to 4.x or newer
warning node-pre-gyp > hawk > sntp > hoek@2.16.3: The major version is no longer supported. Please update to 4.x or newer
warning node-pre-gyp > hawk > boom > hoek@2.16.3: The major version is no longer supported. Please update to 4.x or newer
[2/4] 🚚  Fetching packages...
[3/4] 🔗  Linking dependencies...
[4/4] 📃  Building fresh packages...
success Saved lockfile.
$ node-pre-gyp install --fallback-to-build || node-pre-gyp rebuild
node-pre-gyp info it worked if it ends with ok
node-pre-gyp info using node-pre-gyp@0.6.39
node-pre-gyp info using node@8.11.1 | darwin | x64
node-pre-gyp info check checked for "/Users/banxi/Workspace/OpenCC/build/Release/opencc.node" (not found)
node-pre-gyp http GET https://github.com/BYVoid/OpenCC/releases/download/1.0.5/opencc-v1.0.5-node-v57-darwin-x64.tar.gz
node-pre-gyp http 404 https://github.com/BYVoid/OpenCC/releases/download/1.0.5/opencc-v1.0.5-node-v57-darwin-x64.tar.gz
node-pre-gyp ERR! Tried to download(404): https://github.com/BYVoid/OpenCC/releases/download/1.0.5/opencc-v1.0.5-node-v57-darwin-x64.tar.gz
node-pre-gyp ERR! Pre-built binaries not found for opencc@1.0.5 and node@8.11.1 (node-v57 ABI, unknown) (falling back to source compile with node-gyp)
node-pre-gyp http 404 status code downloading tarball https://github.com/BYVoid/OpenCC/releases/download/1.0.5/opencc-v1.0.5-node-v57-darwin-x64.tar.gz
gyp info it worked if it ends with ok
gyp info using node-gyp@3.6.2
gyp info using node@8.11.1 | darwin | x64
gyp info ok
gyp info it worked if it ends with ok
gyp info using node-gyp@3.6.2
gyp info using node@8.11.1 | darwin | x64
gyp info spawn /usr/bin/python
gyp info spawn args [ '/Users/banxi/.nvm/versions/node/v8.11.1/lib/node_modules/npm/node_modules/node-gyp/gyp/gyp_main.py',
gyp info spawn args   'binding.gyp',
gyp info spawn args   '-f',
gyp info spawn args   'make',
gyp info spawn args   '-I',
gyp info spawn args   '/Users/banxi/Workspace/OpenCC/build/config.gypi',
gyp info spawn args   '-I',
gyp info spawn args   '/Users/banxi/.nvm/versions/node/v8.11.1/lib/node_modules/npm/node_modules/node-gyp/addon.gypi',
gyp info spawn args   '-I',
gyp info spawn args   '/Users/banxi/.node-gyp/8.11.1/include/node/common.gypi',
gyp info spawn args   '-Dlibrary=shared_library',
gyp info spawn args   '-Dvisibility=default',
gyp info spawn args   '-Dnode_root_dir=/Users/banxi/.node-gyp/8.11.1',
gyp info spawn args   '-Dnode_gyp_dir=/Users/banxi/.nvm/versions/node/v8.11.1/lib/node_modules/npm/node_modules/node-gyp',
gyp info spawn args   '-Dnode_lib_file=/Users/banxi/.node-gyp/8.11.1/<(target_arch)/node.lib',
gyp info spawn args   '-Dmodule_root_dir=/Users/banxi/Workspace/OpenCC',
gyp info spawn args   '-Dnode_engine=v8',
gyp info spawn args   '--depth=.',
gyp info spawn args   '--no-parallel',
gyp info spawn args   '--generator-output',
gyp info spawn args   'build',
gyp info spawn args   '-Goutput_dir=.' ]
gyp info ok
gyp info it worked if it ends with ok
gyp info using node-gyp@3.6.2
gyp info using node@8.11.1 | darwin | x64
gyp info spawn make
gyp info spawn args [ 'BUILDTYPE=Release', '-C', 'build' ]
  COPY Release/s2t.json
  COPY Release/t2s.json
  COPY Release/s2tw.json
  COPY Release/s2twp.json
  COPY Release/tw2s.json
  COPY Release/tw2sp.json
  COPY Release/t2tw.json
  COPY Release/s2hk.json
  COPY Release/hk2s.json
  COPY Release/t2hk.json
  TOUCH Release/obj.target/configs.stamp
  CXX(target) Release/obj.target/opencc/node/opencc.o
../node/opencc.cc:122:26: warning: 'Call' is deprecated [-Wdeprecated-declarations]
    conv_data->callback->Call(argc, argv);
                         ^
../node_modules/nan/nan.h:1654:3: note: 'Call' has been explicitly marked deprecated here
  NAN_DEPRECATED inline v8::Local<v8::Value>
  ^
../node_modules/nan/nan.h:102:40: note: expanded from macro 'NAN_DEPRECATED'
# define NAN_DEPRECATED __attribute__((deprecated))
                                       ^
1 warning generated.
  SOLINK_MODULE(target) Release/opencc.node
  ACTION binding_gyp_dicts_target_STCharacters Release/STCharacters.ocd
  ACTION binding_gyp_dicts_target_STPhrases Release/STPhrases.ocd
  ACTION binding_gyp_dicts_target_TSCharacters Release/TSCharacters.ocd
  ACTION binding_gyp_dicts_target_TSPhrases Release/TSPhrases.ocd
  ACTION binding_gyp_dicts_target_TWVariants Release/TWVariants.ocd
  ACTION binding_gyp_dicts_target_TWVariantsRevPhrases Release/TWVariantsRevPhrases.ocd
  ACTION binding_gyp_dicts_target_JPVariants Release/JPVariants.ocd
  ACTION binding_gyp_dicts_target_TWPhrases_txt Release/TWPhrases.txt
  ACTION binding_gyp_dicts_target_TWVariantsRev_txt Release/TWVariantsRev.txt
  ACTION binding_gyp_dicts_target_TWPhrasesRev_txt Release/TWPhrasesRev.txt
  ACTION binding_gyp_dicts_target_TWPhrases Release/TWPhrases.ocd
  ACTION binding_gyp_dicts_target_TWVariantsRev Release/TWVariantsRev.ocd
  ACTION binding_gyp_dicts_target_TWPhrasesRev Release/TWPhrasesRev.ocd
  ACTION binding_gyp_dicts_target_HKVariants Release/HKVariants.ocd
  ACTION binding_gyp_dicts_target_HKVariantsPhrases Release/HKVariantsPhrases.ocd
  ACTION binding_gyp_dicts_target_HKVariantsRevPhrases Release/HKVariantsRevPhrases.ocd
  ACTION binding_gyp_dicts_target_HKVariantsRev_txt Release/HKVariantsRev.txt
  ACTION binding_gyp_dicts_target_HKVariantsRev Release/HKVariantsRev.ocd
  TOUCH Release/obj.target/dicts.stamp
gyp info ok
node-pre-gyp info ok
✨  Done in 25.26s.
➜  OpenCC (master) ✗ make node
node-gyp configure
make: node-gyp: No such file or directory
make: *** [node] Error 1
```

## 执行单元测试

```
➜  OpenCC (master) ✗ make test
mkdir -p build/dbg/root
(cd build/dbg; cmake \
	-DBUILD_DOCUMENTATION:BOOL=OFF \
	-DENABLE_GTEST:BOOL=ON \
	-DCMAKE_BUILD_TYPE=Debug \
	-DCMAKE_INSTALL_PREFIX=`pwd`/root \
	../..)
-- The CXX compiler identification is AppleClang 10.0.0.10001145
-- Check for working CXX compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++
-- Check for working CXX compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Performing Test COMPILER_HAS_HIDDEN_VISIBILITY
-- Performing Test COMPILER_HAS_HIDDEN_VISIBILITY - Success
-- Performing Test COMPILER_HAS_HIDDEN_INLINE_VISIBILITY
-- Performing Test COMPILER_HAS_HIDDEN_INLINE_VISIBILITY - Success
-- Performing Test COMPILER_HAS_DEPRECATED_ATTR
-- Performing Test COMPILER_HAS_DEPRECATED_ATTR - Success
-- The C compiler identification is AppleClang 10.0.0.10001145
-- Check for working C compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc
-- Check for working C compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Found PythonInterp: /usr/bin/python (found version "2.7.10")
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Looking for pthread_create
-- Looking for pthread_create - found
-- Found Threads: TRUE
-- Configuring done
-- Generating done
-- Build files have been written to: /Users/banxi/Workspace/OpenCC/build/dbg
make -C build/dbg VERBOSE=
Dependee "/Users/banxi/Workspace/OpenCC/build/dbg/deps/gtest-1.7.0/CMakeFiles/gtest.dir/DependInfo.cmake" is newer than depender "/Users/banxi/Workspace/OpenCC/build/dbg/deps/gtest-1.7.0/CMakeFiles/gtest.dir/depend.internal".
Dependee "/Users/banxi/Workspace/OpenCC/build/dbg/deps/gtest-1.7.0/CMakeFiles/CMakeDirectoryInformation.cmake" is newer than depender "/Users/banxi/Workspace/OpenCC/build/dbg/deps/gtest-1.7.0/CMakeFiles/gtest.dir/depend.internal".
Scanning dependencies of target gtest
[  1%] Building CXX object deps/gtest-1.7.0/CMakeFiles/gtest.dir/src/gtest-all.cc.o
[  3%] Linking CXX shared library libgtest.dylib
ld: warning: directory not found for option '-L/Users/banxi/Workspace/OpenCC/build/dbg/deps/gtest-1.7.0/src'
[  3%] Built target gtest
Dependee "/Users/banxi/Workspace/OpenCC/build/dbg/src/CMakeFiles/libopencc.dir/DependInfo.cmake" is newer than depender "/Users/banxi/Workspace/OpenCC/build/dbg/src/CMakeFiles/libopencc.dir/depend.internal".
Dependee "/Users/banxi/Workspace/OpenCC/build/dbg/src/CMakeFiles/CMakeDirectoryInformation.cmake" is newer than depender "/Users/banxi/Workspace/OpenCC/build/dbg/src/CMakeFiles/libopencc.dir/depend.internal".
Scanning dependencies of target libopencc
[  4%] Building CXX object src/CMakeFiles/libopencc.dir/BinaryDict.cpp.o
[  6%] Building CXX object src/CMakeFiles/libopencc.dir/Config.cpp.o
[  8%] Building CXX object src/CMakeFiles/libopencc.dir/Conversion.cpp.o
[  9%] Building CXX object src/CMakeFiles/libopencc.dir/ConversionChain.cpp.o
[ 11%] Building CXX object src/CMakeFiles/libopencc.dir/Converter.cpp.o
[ 13%] Building CXX object src/CMakeFiles/libopencc.dir/DartsDict.cpp.o
[ 14%] Building CXX object src/CMakeFiles/libopencc.dir/Dict.cpp.o
[ 16%] Building CXX object src/CMakeFiles/libopencc.dir/DictConverter.cpp.o
[ 18%] Building CXX object src/CMakeFiles/libopencc.dir/DictEntry.cpp.o
[ 19%] Building CXX object src/CMakeFiles/libopencc.dir/DictGroup.cpp.o
[ 21%] Building CXX object src/CMakeFiles/libopencc.dir/MaxMatchSegmentation.cpp.o
[ 22%] Building CXX object src/CMakeFiles/libopencc.dir/PhraseExtract.cpp.o
[ 24%] Building CXX object src/CMakeFiles/libopencc.dir/SimpleConverter.cpp.o
[ 26%] Building CXX object src/CMakeFiles/libopencc.dir/Segmentation.cpp.o
[ 27%] Building CXX object src/CMakeFiles/libopencc.dir/TextDict.cpp.o
[ 29%] Building CXX object src/CMakeFiles/libopencc.dir/UTF8StringSlice.cpp.o
[ 31%] Building CXX object src/CMakeFiles/libopencc.dir/UTF8Util.cpp.o
[ 32%] Linking CXX shared library libopencc.dylib
[ 32%] Built target libopencc
Dependee "/Users/banxi/Workspace/OpenCC/build/dbg/deps/gtest-1.7.0/CMakeFiles/gtest_main.dir/DependInfo.cmake" is newer than depender "/Users/banxi/Workspace/OpenCC/build/dbg/deps/gtest-1.7.0/CMakeFiles/gtest_main.dir/depend.internal".
Dependee "/Users/banxi/Workspace/OpenCC/build/dbg/deps/gtest-1.7.0/CMakeFiles/CMakeDirectoryInformation.cmake" is newer than depender "/Users/banxi/Workspace/OpenCC/build/dbg/deps/gtest-1.7.0/CMakeFiles/gtest_main.dir/depend.internal".
Scanning dependencies of target gtest_main
[ 34%] Building CXX object deps/gtest-1.7.0/CMakeFiles/gtest_main.dir/src/gtest_main.cc.o
[ 36%] Linking CXX shared library libgtest_main.dylib
ld: warning: directory not found for option '-L/Users/banxi/Workspace/OpenCC/build/dbg/deps/gtest-1.7.0/src'
[ 36%] Built target gtest_main
Dependee "/Users/banxi/Workspace/OpenCC/build/dbg/src/CMakeFiles/UnitTest.dir/DependInfo.cmake" is newer than depender "/Users/banxi/Workspace/OpenCC/build/dbg/src/CMakeFiles/UnitTest.dir/depend.internal".
Dependee "/Users/banxi/Workspace/OpenCC/build/dbg/src/CMakeFiles/CMakeDirectoryInformation.cmake" is newer than depender "/Users/banxi/Workspace/OpenCC/build/dbg/src/CMakeFiles/UnitTest.dir/depend.internal".
Scanning dependencies of target UnitTest
[ 37%] Building CXX object src/CMakeFiles/UnitTest.dir/BinaryDictTest.cpp.o
[ 39%] Building CXX object src/CMakeFiles/UnitTest.dir/ConfigTest.cpp.o
[ 40%] Building CXX object src/CMakeFiles/UnitTest.dir/ConversionChainTest.cpp.o
[ 42%] Building CXX object src/CMakeFiles/UnitTest.dir/ConversionTest.cpp.o
[ 44%] Building CXX object src/CMakeFiles/UnitTest.dir/DartsDictTest.cpp.o
[ 45%] Building CXX object src/CMakeFiles/UnitTest.dir/DictGroupTest.cpp.o
[ 47%] Building CXX object src/CMakeFiles/UnitTest.dir/MaxMatchSegmentationTest.cpp.o
[ 49%] Building CXX object src/CMakeFiles/UnitTest.dir/PhraseExtractTest.cpp.o
[ 50%] Building CXX object src/CMakeFiles/UnitTest.dir/SimpleConverterTest.cpp.o
[ 52%] Building CXX object src/CMakeFiles/UnitTest.dir/TextDictTest.cpp.o
[ 54%] Building CXX object src/CMakeFiles/UnitTest.dir/UTF8StringSliceTest.cpp.o
[ 55%] Building CXX object src/CMakeFiles/UnitTest.dir/UTF8UtilTest.cpp.o
[ 57%] Linking CXX executable UnitTest
[ 57%] Built target UnitTest
Dependee "/Users/banxi/Workspace/OpenCC/build/dbg/src/tools/CMakeFiles/opencc_phrase_extract.dir/DependInfo.cmake" is newer than depender "/Users/banxi/Workspace/OpenCC/build/dbg/src/tools/CMakeFiles/opencc_phrase_extract.dir/depend.internal".
Dependee "/Users/banxi/Workspace/OpenCC/build/dbg/src/tools/CMakeFiles/CMakeDirectoryInformation.cmake" is newer than depender "/Users/banxi/Workspace/OpenCC/build/dbg/src/tools/CMakeFiles/opencc_phrase_extract.dir/depend.internal".
Scanning dependencies of target opencc_phrase_extract
[ 59%] Building CXX object src/tools/CMakeFiles/opencc_phrase_extract.dir/PhraseExtract.cpp.o
[ 60%] Linking CXX executable opencc_phrase_extract
[ 60%] Built target opencc_phrase_extract
Dependee "/Users/banxi/Workspace/OpenCC/build/dbg/src/tools/CMakeFiles/opencc_dict.dir/DependInfo.cmake" is newer than depender "/Users/banxi/Workspace/OpenCC/build/dbg/src/tools/CMakeFiles/opencc_dict.dir/depend.internal".
Dependee "/Users/banxi/Workspace/OpenCC/build/dbg/src/tools/CMakeFiles/CMakeDirectoryInformation.cmake" is newer than depender "/Users/banxi/Workspace/OpenCC/build/dbg/src/tools/CMakeFiles/opencc_dict.dir/depend.internal".
Scanning dependencies of target opencc_dict
[ 62%] Building CXX object src/tools/CMakeFiles/opencc_dict.dir/DictConverter.cpp.o
[ 63%] Linking CXX executable opencc_dict
[ 63%] Built target opencc_dict
Dependee "/Users/banxi/Workspace/OpenCC/build/dbg/src/tools/CMakeFiles/opencc.dir/DependInfo.cmake" is newer than depender "/Users/banxi/Workspace/OpenCC/build/dbg/src/tools/CMakeFiles/opencc.dir/depend.internal".
Dependee "/Users/banxi/Workspace/OpenCC/build/dbg/src/tools/CMakeFiles/CMakeDirectoryInformation.cmake" is newer than depender "/Users/banxi/Workspace/OpenCC/build/dbg/src/tools/CMakeFiles/opencc.dir/depend.internal".
Scanning dependencies of target opencc
[ 65%] Building CXX object src/tools/CMakeFiles/opencc.dir/CommandLine.cpp.o
/Users/banxi/Workspace/OpenCC/src/tools/CommandLine.cpp:87:38: warning: 'tmpnam' is deprecated: This function is
      provided for compatibility reasons only. Due to security concerns inherent in the design of tmpnam(3), it is
      highly recommended that you use mkstemp(3) instead. [-Wdeprecated-declarations]
    const string tempFileName = std::tmpnam(nullptr);
                                     ^
/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.14.sdk/usr/include/stdio.h:186:1: note:
      'tmpnam' has been explicitly marked deprecated here
__deprecated_msg("This function is provided for compatibility reasons only.  Due to security concerns inher...
^
/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.14.sdk/usr/include/sys/cdefs.h:180:48: note:
      expanded from macro '__deprecated_msg'
        #define __deprecated_msg(_msg) __attribute__((deprecated(_msg)))
                                                      ^
1 warning generated.
[ 67%] Linking CXX executable opencc
[ 67%] Built target opencc
Dependee "/Users/banxi/Workspace/OpenCC/build/dbg/data/CMakeFiles/Dictionaries.dir/DependInfo.cmake" is newer than depender "/Users/banxi/Workspace/OpenCC/build/dbg/data/CMakeFiles/Dictionaries.dir/depend.internal".
Dependee "/Users/banxi/Workspace/OpenCC/build/dbg/data/CMakeFiles/CMakeDirectoryInformation.cmake" is newer than depender "/Users/banxi/Workspace/OpenCC/build/dbg/data/CMakeFiles/Dictionaries.dir/depend.internal".
Scanning dependencies of target Dictionaries
[ 68%] Building STCharacters.ocd
[ 70%] Building STPhrases.ocd
[ 72%] Building TSCharacters.ocd
[ 73%] Building TSPhrases.ocd
[ 75%] Building TWVariants.ocd
[ 77%] Building TWVariantsRevPhrases.ocd
[ 78%] Building JPVariants.ocd
[ 80%] Building HKVariants.ocd
[ 81%] Building HKVariantsPhrases.ocd
[ 83%] Building HKVariantsRevPhrases.ocd
[ 85%] Generating TWPhrases.txt
[ 86%] Building TWPhrases.ocd
[ 88%] Generating TWPhrasesRev.txt
[ 90%] Building TWPhrasesRev.ocd
[ 91%] Generating TWVariantsRev.txt
[ 93%] Building TWVariantsRev.ocd
[ 95%] Generating HKVariantsRev.txt
[ 96%] Building HKVariantsRev.ocd
[ 96%] Built target Dictionaries
Dependee "/Users/banxi/Workspace/OpenCC/build/dbg/test/CMakeFiles/CommandLineConvertTest.dir/DependInfo.cmake" is newer than depender "/Users/banxi/Workspace/OpenCC/build/dbg/test/CMakeFiles/CommandLineConvertTest.dir/depend.internal".
Dependee "/Users/banxi/Workspace/OpenCC/build/dbg/test/CMakeFiles/CMakeDirectoryInformation.cmake" is newer than depender "/Users/banxi/Workspace/OpenCC/build/dbg/test/CMakeFiles/CommandLineConvertTest.dir/depend.internal".
Scanning dependencies of target CommandLineConvertTest
[ 98%] Building CXX object test/CMakeFiles/CommandLineConvertTest.dir/CommandLineConvertTest.cpp.o
[100%] Linking CXX executable CommandLineConvertTest
[100%] Built target CommandLineConvertTest
(cd build/dbg; ctest --verbose)
UpdateCTestConfiguration  from :/Users/banxi/Workspace/OpenCC/build/dbg/DartConfiguration.tcl
Parse Config file:/Users/banxi/Workspace/OpenCC/build/dbg/DartConfiguration.tcl
UpdateCTestConfiguration  from :/Users/banxi/Workspace/OpenCC/build/dbg/DartConfiguration.tcl
Parse Config file:/Users/banxi/Workspace/OpenCC/build/dbg/DartConfiguration.tcl
Test project /Users/banxi/Workspace/OpenCC/build/dbg
Constructing a list of tests
Done constructing a list of tests
Updating test list for fixtures
Added 0 tests to meet fixture requirements
Checking test dependency graph...
Checking test dependency graph end
test 1
    Start 1: UnitTest

1: Test command: /Users/banxi/Workspace/OpenCC/build/dbg/src/UnitTest
1: Test timeout computed to be: 1500
1: Running main() from gtest_main.cc
1: [==========] Running 47 tests from 12 test cases.
1: [----------] Global test environment set-up.
1: [----------] 2 tests from BinaryDictTest
1: [ RUN      ] BinaryDictTest.Serialization
1: [       OK ] BinaryDictTest.Serialization (0 ms)
1: [ RUN      ] BinaryDictTest.Deserialization
1: [       OK ] BinaryDictTest.Deserialization (1 ms)
1: [----------] 2 tests from BinaryDictTest (1 ms total)
1:
1: [----------] 4 tests from ConfigTest
1: [ RUN      ] ConfigTest.Convert
1: [       OK ] ConfigTest.Convert (0 ms)
1: [ RUN      ] ConfigTest.ConvertBuffer
1: [       OK ] ConfigTest.ConvertBuffer (0 ms)
1: [ RUN      ] ConfigTest.NonexistingPath
1: [       OK ] ConfigTest.NonexistingPath (1 ms)
1: [ RUN      ] ConfigTest.NewFromStringWitoutTrailingSlash
1: [       OK ] ConfigTest.NewFromStringWitoutTrailingSlash (0 ms)
1: [----------] 4 tests from ConfigTest (1 ms total)
1:
1: [----------] 1 test from ConversionChainTest
1: [ RUN      ] ConversionChainTest.Convert
1: [       OK ] ConversionChainTest.Convert (0 ms)
1: [----------] 1 test from ConversionChainTest (0 ms total)
1:
1: [----------] 2 tests from ConversionTest
1: [ RUN      ] ConversionTest.ConvertString
1: [       OK ] ConversionTest.ConvertString (0 ms)
1: [ RUN      ] ConversionTest.ConvertCString
1: [       OK ] ConversionTest.ConvertCString (0 ms)
1: [----------] 2 tests from ConversionTest (0 ms total)
1:
1: [----------] 3 tests from DartsDictTest
1: [ RUN      ] DartsDictTest.DictTest
1: [       OK ] DartsDictTest.DictTest (0 ms)
1: [ RUN      ] DartsDictTest.Serialization
1: [       OK ] DartsDictTest.Serialization (1 ms)
1: [ RUN      ] DartsDictTest.Deserialization
1: [       OK ] DartsDictTest.Deserialization (0 ms)
1: [----------] 3 tests from DartsDictTest (1 ms total)
1:
1: [----------] 2 tests from DictGroupTest
1: [ RUN      ] DictGroupTest.SimpleGroupTest
1: [       OK ] DictGroupTest.SimpleGroupTest (0 ms)
1: [ RUN      ] DictGroupTest.TaiwanPhraseGroupTest
1: [       OK ] DictGroupTest.TaiwanPhraseGroupTest (0 ms)
1: [----------] 2 tests from DictGroupTest (0 ms total)
1:
1: [----------] 1 test from MaxMatchSegmentationTest
1: [ RUN      ] MaxMatchSegmentationTest.Segment
1: [       OK ] MaxMatchSegmentationTest.Segment (0 ms)
1: [----------] 1 test from MaxMatchSegmentationTest (0 ms total)
1:
1: [----------] 9 tests from PhraseExtractTest
1: [ RUN      ] PhraseExtractTest.ExtractSuffixes
1: [       OK ] PhraseExtractTest.ExtractSuffixes (0 ms)
1: [ RUN      ] PhraseExtractTest.ExtractPrefixes
1: [       OK ] PhraseExtractTest.ExtractPrefixes (0 ms)
1: [ RUN      ] PhraseExtractTest.CalculateFrequency
1: [       OK ] PhraseExtractTest.CalculateFrequency (0 ms)
1: [ RUN      ] PhraseExtractTest.ExtractWordCandidates
1: [       OK ] PhraseExtractTest.ExtractWordCandidates (1 ms)
1: [ RUN      ] PhraseExtractTest.CalculateCohesions
1: [       OK ] PhraseExtractTest.CalculateCohesions (0 ms)
1: [ RUN      ] PhraseExtractTest.CalculateSuffixEntropy
1: [       OK ] PhraseExtractTest.CalculateSuffixEntropy (0 ms)
1: [ RUN      ] PhraseExtractTest.CalculatePrefixEntropy
1: [       OK ] PhraseExtractTest.CalculatePrefixEntropy (0 ms)
1: [ RUN      ] PhraseExtractTest.SelectWords
1: [       OK ] PhraseExtractTest.SelectWords (1 ms)
1: [ RUN      ] PhraseExtractTest.Punctuation
1: [       OK ] PhraseExtractTest.Punctuation (0 ms)
1: [----------] 9 tests from PhraseExtractTest (2 ms total)
1:
1: [----------] 3 tests from SimpleConverterTest
1: [ RUN      ] SimpleConverterTest.Convert
1: [       OK ] SimpleConverterTest.Convert (0 ms)
1: [ RUN      ] SimpleConverterTest.Multithreading
1: [       OK ] SimpleConverterTest.Multithreading (0 ms)
1: [ RUN      ] SimpleConverterTest.CInterface
1: [       OK ] SimpleConverterTest.CInterface (0 ms)
1: [----------] 3 tests from SimpleConverterTest (1 ms total)
1:
1: [----------] 3 tests from TextDictTest
1: [ RUN      ] TextDictTest.DictTest
1: [       OK ] TextDictTest.DictTest (0 ms)
1: [ RUN      ] TextDictTest.Serialization
1: [       OK ] TextDictTest.Serialization (1 ms)
1: [ RUN      ] TextDictTest.Deserialization
1: [       OK ] TextDictTest.Deserialization (0 ms)
1: [----------] 3 tests from TextDictTest (1 ms total)
1:
1: [----------] 11 tests from UTF8StringSliceTest
1: [ RUN      ] UTF8StringSliceTest.UTF8Length
1: [       OK ] UTF8StringSliceTest.UTF8Length (0 ms)
1: [ RUN      ] UTF8StringSliceTest.ByteLength
1: [       OK ] UTF8StringSliceTest.ByteLength (0 ms)
1: [ RUN      ] UTF8StringSliceTest.Left
1: [       OK ] UTF8StringSliceTest.Left (0 ms)
1: [ RUN      ] UTF8StringSliceTest.Right
1: [       OK ] UTF8StringSliceTest.Right (0 ms)
1: [ RUN      ] UTF8StringSliceTest.SubString
1: [       OK ] UTF8StringSliceTest.SubString (0 ms)
1: [ RUN      ] UTF8StringSliceTest.ToString
1: [       OK ] UTF8StringSliceTest.ToString (0 ms)
1: [ RUN      ] UTF8StringSliceTest.Compare
1: [       OK ] UTF8StringSliceTest.Compare (0 ms)
1: [ RUN      ] UTF8StringSliceTest.MoveRight
1: [       OK ] UTF8StringSliceTest.MoveRight (0 ms)
1: [ RUN      ] UTF8StringSliceTest.MoveLeft
1: [       OK ] UTF8StringSliceTest.MoveLeft (0 ms)
1: [ RUN      ] UTF8StringSliceTest.ReverseCompare
1: [       OK ] UTF8StringSliceTest.ReverseCompare (0 ms)
1: [ RUN      ] UTF8StringSliceTest.FindBytePosition
1: [       OK ] UTF8StringSliceTest.FindBytePosition (0 ms)
1: [----------] 11 tests from UTF8StringSliceTest (0 ms total)
1:
1: [----------] 6 tests from UTF8UtilTest
1: [ RUN      ] UTF8UtilTest.NextCharLength
1: [       OK ] UTF8UtilTest.NextCharLength (0 ms)
1: [ RUN      ] UTF8UtilTest.PrevCharLength
1: [       OK ] UTF8UtilTest.PrevCharLength (0 ms)
1: [ RUN      ] UTF8UtilTest.Length
1: [       OK ] UTF8UtilTest.Length (0 ms)
1: [ RUN      ] UTF8UtilTest.NotShorterThan
1: [       OK ] UTF8UtilTest.NotShorterThan (0 ms)
1: [ RUN      ] UTF8UtilTest.TruncateUTF8
1: [       OK ] UTF8UtilTest.TruncateUTF8 (0 ms)
1: [ RUN      ] UTF8UtilTest.GetByteMap
1: [       OK ] UTF8UtilTest.GetByteMap (0 ms)
1: [----------] 6 tests from UTF8UtilTest (0 ms total)
1:
1: [----------] Global test environment tear-down
1: [==========] 47 tests from 12 test cases ran. (7 ms total)
1: [  PASSED  ] 47 tests.
1/2 Test #1: UnitTest .........................   Passed    0.02 sec
test 2
    Start 2: CommandLineConvertTest

2: Test command: /Users/banxi/Workspace/OpenCC/build/dbg/test/CommandLineConvertTest
2: Test timeout computed to be: 1500
2: Running main() from gtest_main.cc
2: [==========] Running 8 tests from 1 test case.
2: [----------] Global test environment set-up.
2: [----------] 8 tests from CommandLine/ConfigurationTest
2: [ RUN      ] CommandLine/ConfigurationTest.Convert/0
2: [       OK ] CommandLine/ConfigurationTest.Convert/0 (59 ms)
2: [ RUN      ] CommandLine/ConfigurationTest.Convert/1
2: [       OK ] CommandLine/ConfigurationTest.Convert/1 (14 ms)
2: [ RUN      ] CommandLine/ConfigurationTest.Convert/2
2: [       OK ] CommandLine/ConfigurationTest.Convert/2 (61 ms)
2: [ RUN      ] CommandLine/ConfigurationTest.Convert/3
2: [       OK ] CommandLine/ConfigurationTest.Convert/3 (62 ms)
2: [ RUN      ] CommandLine/ConfigurationTest.Convert/4
2: [       OK ] CommandLine/ConfigurationTest.Convert/4 (13 ms)
2: [ RUN      ] CommandLine/ConfigurationTest.Convert/5
2: [       OK ] CommandLine/ConfigurationTest.Convert/5 (13 ms)
2: [ RUN      ] CommandLine/ConfigurationTest.Convert/6
2: [       OK ] CommandLine/ConfigurationTest.Convert/6 (63 ms)
2: [ RUN      ] CommandLine/ConfigurationTest.Convert/7
2: [       OK ] CommandLine/ConfigurationTest.Convert/7 (14 ms)
2: [----------] 8 tests from CommandLine/ConfigurationTest (299 ms total)
2:
2: [----------] Global test environment tear-down
2: [==========] 8 tests from 1 test case ran. (299 ms total)
2: [  PASSED  ] 8 tests.
2/2 Test #2: CommandLineConvertTest ...........   Passed    0.30 sec

100% tests passed, 0 tests failed out of 2

Total Test time (real) =   0.33 sec
make -C build/dbg install VERBOSE=
[  3%] Built target gtest
[ 32%] Built target libopencc
[ 36%] Built target gtest_main
[ 57%] Built target UnitTest
[ 60%] Built target opencc_phrase_extract
[ 63%] Built target opencc_dict
[ 67%] Built target opencc
[ 96%] Built target Dictionaries
[100%] Built target CommandLineConvertTest
Install the project...
-- Install configuration: "Debug"
-- Installing: /Users/banxi/Workspace/OpenCC/build/dbg/root/lib/pkgconfig/opencc.pc
-- Installing: /Users/banxi/Workspace/OpenCC/build/dbg/root/lib/libopencc.1.0.0.dylib
-- Installing: /Users/banxi/Workspace/OpenCC/build/dbg/root/lib/libopencc.2.dylib
-- Installing: /Users/banxi/Workspace/OpenCC/build/dbg/root/lib/libopencc.dylib
-- Installing: /Users/banxi/Workspace/OpenCC/build/dbg/root/include/opencc/BinaryDict.hpp
-- Installing: /Users/banxi/Workspace/OpenCC/build/dbg/root/include/opencc/Common.hpp
-- Installing: /Users/banxi/Workspace/OpenCC/build/dbg/root/include/opencc/Config.hpp
-- Installing: /Users/banxi/Workspace/OpenCC/build/dbg/root/include/opencc/Conversion.hpp
-- Installing: /Users/banxi/Workspace/OpenCC/build/dbg/root/include/opencc/ConversionChain.hpp
-- Installing: /Users/banxi/Workspace/OpenCC/build/dbg/root/include/opencc/Converter.hpp
-- Installing: /Users/banxi/Workspace/OpenCC/build/dbg/root/include/opencc/DartsDict.hpp
-- Installing: /Users/banxi/Workspace/OpenCC/build/dbg/root/include/opencc/Dict.hpp
-- Installing: /Users/banxi/Workspace/OpenCC/build/dbg/root/include/opencc/DictConverter.hpp
-- Installing: /Users/banxi/Workspace/OpenCC/build/dbg/root/include/opencc/DictEntry.hpp
-- Installing: /Users/banxi/Workspace/OpenCC/build/dbg/root/include/opencc/DictGroup.hpp
-- Installing: /Users/banxi/Workspace/OpenCC/build/dbg/root/include/opencc/Exception.hpp
-- Installing: /Users/banxi/Workspace/OpenCC/build/dbg/root/include/opencc/Export.hpp
-- Installing: /Users/banxi/Workspace/OpenCC/build/dbg/root/include/opencc/Lexicon.hpp
-- Installing: /Users/banxi/Workspace/OpenCC/build/dbg/root/include/opencc/MaxMatchSegmentation.hpp
-- Installing: /Users/banxi/Workspace/OpenCC/build/dbg/root/include/opencc/Optional.hpp
-- Installing: /Users/banxi/Workspace/OpenCC/build/dbg/root/include/opencc/PhraseExtract.hpp
-- Installing: /Users/banxi/Workspace/OpenCC/build/dbg/root/include/opencc/Segmentation.hpp
-- Installing: /Users/banxi/Workspace/OpenCC/build/dbg/root/include/opencc/Segments.hpp
-- Installing: /Users/banxi/Workspace/OpenCC/build/dbg/root/include/opencc/SerializableDict.hpp
-- Installing: /Users/banxi/Workspace/OpenCC/build/dbg/root/include/opencc/SimpleConverter.hpp
-- Installing: /Users/banxi/Workspace/OpenCC/build/dbg/root/include/opencc/TextDict.hpp
-- Installing: /Users/banxi/Workspace/OpenCC/build/dbg/root/include/opencc/UTF8StringSlice.hpp
-- Installing: /Users/banxi/Workspace/OpenCC/build/dbg/root/include/opencc/UTF8Util.hpp
-- Installing: /Users/banxi/Workspace/OpenCC/build/dbg/root/include/opencc/opencc.h
-- Installing: /Users/banxi/Workspace/OpenCC/build/dbg/root/bin/opencc
-- Installing: /Users/banxi/Workspace/OpenCC/build/dbg/root/bin/opencc_dict
-- Installing: /Users/banxi/Workspace/OpenCC/build/dbg/root/bin/opencc_phrase_extract
-- Installing: /Users/banxi/Workspace/OpenCC/build/dbg/root/share/opencc/STCharacters.ocd
-- Installing: /Users/banxi/Workspace/OpenCC/build/dbg/root/share/opencc/STPhrases.ocd
-- Installing: /Users/banxi/Workspace/OpenCC/build/dbg/root/share/opencc/TSCharacters.ocd
-- Installing: /Users/banxi/Workspace/OpenCC/build/dbg/root/share/opencc/TSPhrases.ocd
-- Installing: /Users/banxi/Workspace/OpenCC/build/dbg/root/share/opencc/TWVariants.ocd
-- Installing: /Users/banxi/Workspace/OpenCC/build/dbg/root/share/opencc/TWVariantsRevPhrases.ocd
-- Installing: /Users/banxi/Workspace/OpenCC/build/dbg/root/share/opencc/JPVariants.ocd
-- Installing: /Users/banxi/Workspace/OpenCC/build/dbg/root/share/opencc/HKVariants.ocd
-- Installing: /Users/banxi/Workspace/OpenCC/build/dbg/root/share/opencc/HKVariantsPhrases.ocd
-- Installing: /Users/banxi/Workspace/OpenCC/build/dbg/root/share/opencc/HKVariantsRevPhrases.ocd
-- Installing: /Users/banxi/Workspace/OpenCC/build/dbg/root/share/opencc/TWPhrases.ocd
-- Installing: /Users/banxi/Workspace/OpenCC/build/dbg/root/share/opencc/TWPhrasesRev.ocd
-- Installing: /Users/banxi/Workspace/OpenCC/build/dbg/root/share/opencc/TWVariantsRev.ocd
-- Installing: /Users/banxi/Workspace/OpenCC/build/dbg/root/share/opencc/HKVariantsRev.ocd
-- Installing: /Users/banxi/Workspace/OpenCC/build/dbg/root/share/opencc/s2t.json
-- Installing: /Users/banxi/Workspace/OpenCC/build/dbg/root/share/opencc/t2s.json
-- Installing: /Users/banxi/Workspace/OpenCC/build/dbg/root/share/opencc/s2tw.json
-- Installing: /Users/banxi/Workspace/OpenCC/build/dbg/root/share/opencc/s2twp.json
-- Installing: /Users/banxi/Workspace/OpenCC/build/dbg/root/share/opencc/tw2s.json
-- Installing: /Users/banxi/Workspace/OpenCC/build/dbg/root/share/opencc/tw2sp.json
-- Installing: /Users/banxi/Workspace/OpenCC/build/dbg/root/share/opencc/t2tw.json
-- Installing: /Users/banxi/Workspace/OpenCC/build/dbg/root/share/opencc/s2hk.json
-- Installing: /Users/banxi/Workspace/OpenCC/build/dbg/root/share/opencc/hk2s.json
-- Installing: /Users/banxi/Workspace/OpenCC/build/dbg/root/share/opencc/t2hk.json
```
