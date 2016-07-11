# erikng-recipes
Finally writing Autopkg recipes

## Notes about Genymotion
Genymotion requires a custom processor due to the fact that their update model/api is entirely proprietary. Genymotion also does not use proper versioning on their applications, so I opted to use munki's native md5 hash feature. This allows us to not repackage the vendor's DMG.
