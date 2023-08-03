exports.createPages = async({ actions }) => {
  const fs = require('fs')
  const { createPage } = actions
  const dir = __dirname + '/src/data/'
  const timelineTemplate = require.resolve(`./src/templates/timeline.js`)

  fs.readdirSync(dir).forEach((file) => {
    if (!file) {
      return
    }

    const data = fs.readFileSync(dir + file, 'utf8', (err, jsonString) => {
      if (err) {
          console.log("File read failed:", err)
          return 
      }
      return jsonString
    })

    createPage({
      path: file.replace(/\.json$/, ''),
      component: timelineTemplate,
      context: {
          // additional data can be passed via context
          data: JSON.parse(data)
      },
    })
  });
}