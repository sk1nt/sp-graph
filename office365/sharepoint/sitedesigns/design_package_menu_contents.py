from office365.sharepoint.entity import Entity


class DesignPackageMenuContents(Entity):
    @property
    def entity_type_name(self):
        return "Microsoft.SharePoint.Utilities.WebTemplateExtensions.DesignPackageMenuContents"
