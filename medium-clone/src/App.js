// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Home from './components/Home';
import Article from './components/Article';
import CreateArticle from './components/CreateArticle';

function App() {
  return (
    <Router>
      <div className="App">
        <Switch>
          <Route path="/" exact component={Home} />
          <Route path="/article/:id" component={Article} />
          <Route path="/create" component={CreateArticle} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;
