#cloud-config

package_update: true
package_upgrade: true

packages:
  - nginx

runcmd:
  - systemctl enable nginx
  - systemctl start nginx
  - echo "Welcome to Nginx on Azure VMSS" > /var/www/html/index.html
