mkdir build
pip install --quiet -t ./build -r requirements.txt
cp ./src/* ./build/

find ./build -type d -print0 | xargs -0 chmod ugo+rx && \
find ./build -type f -print0 | xargs -0 chmod ugo+r

python -m compileall -q ./build

cd build
zip --quiet -9r ../${ZIPFILE:-lambda.zip} .
cd ..
rm -rf build