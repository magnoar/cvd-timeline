import React from 'react'

import Layout from "../components/layout"
import SEO from "../components/seo"
import "../components/timeline.scss"


const Timeline = ({pageContext}) => {

  return (
    <Layout>
      <SEO title="Home" />
      <main>
        {
          pageContext.data.map((item, index) => {
            return (
              <div key={`item_${index}`} className="item">
                <div>{ item.date }</div>
                <div><h3>{ item.title }</h3></div>
                <div>{ item.text }</div>
                <div><a href={ item.source }>{ item.source }</a></div>
              </div>
            )
          })
        }
      </main>
    </Layout>
  )
}

export default Timeline;

