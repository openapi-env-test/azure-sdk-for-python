# autorest configuration for Python

### Settings

``` yaml 
clear-output-folder: true
license-header: MICROSOFT_MIT_NO_VERSION
no-namespace-folders: true
package-name: azure-purview-administration
package-version: 1.0.0b1
require:
- ../../../../../azure-rest-api-specs/specification/purview/data-plane/readme.md
version-tolerant: true
```

### Python multi-client

``` yaml 
batch:
- purview-account: true
- purview-metadata: true
```

### Tag: purview-account

``` yaml $(purview-account)
namespace: azure.purview.administration.account
output-folder: ../azure/purview/administration/account
```

### Tag: purview-metadata

``` yaml $(purview-metadata)
namespace: azure.purview.administration.metadata
output-folder: ../azure/purview/administration/metadata
```
