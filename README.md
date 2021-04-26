![banner.js](static/banner.png)

**elekto** is a flask based web application for conducting online elections. It is built specifically for opensource organisations to help run them steering and community elections.

Elekto was inspired by the long-running [CIVS](https://civs.cs.cornell.edu) project and built to conduct kubernetes steering and community elections. The project was created as the part of [The Linux Foundation's Internship](https://docs.linuxfoundation.org/lfx/mentorship) and now it's hosted and maintained by [Cloud Native Computing Foundation](https://github.com/cncf/).

Elekto is currently used by [Kubernetes](https://github.com/kubernetes/), [Knative](https://github.com/knative/) and [more](https://elekto.io/#td-block-5).

# Features

Elekto was designed to support the following:

- 100% GitOps workflow for configuration and election administration
- 100% Oauth-driven workflow for voters (no emails)
- Preference election voting (starting with [condorcet](https://en.wikipedia.org/wiki/Condorcet_method))
- Multiple elections for the same organization
- Responsive web design
- Secret ballot voting


# Getting Started
See our documentation on [elekto.io](https://elekto.io/docs).


Create an `.env` file from `.env.example` by running `cp .env.example .env` and update the necessary entires (see [here](https://elekto.io/docs/getting-started/) for more information on env parameters).

If you want to run elekto right away there are two options:

**You have a working conda environment.**

Create an elekto environment
```bash
conda env create -f environment.yml
```

Run the application using 
```bash
python console run
```

**You have a working Docker environment.**

You can run this application inside a Docker container. This approach doesn't require you to install any dependencies other than Docker.

Build the docker image
```bash
docker build -f dev.Dockerfile -t elekto:dev .
```

Run the built image
```bash

docker run -d -p 5000:5000 --name="eleko" elekto:dev
```

Open your web browser and type http://localhost:5000 in your navigation bar, This opens a local instance of the elekto application's login page. 

<!-- You can now make changes to the docsy example and those changes will immediately show up in your browser after you save. -->

<!-- To stop the container, first identify the container ID with:

```bash
docker container ls
```

Take note of the hexadecimal string below the CONTAINER ID column, then stop the container:

```bash
docker stop [container_id]
```

To delete the container run:

```bash
docker container rm [container_id]
``` -->

For the full story, head over to the developer's documentation.


# Getting Help

The elekto project is maintained by Manish Sahani and Josh Berkus, Reach out to us one way or another.


# Contributing 

We're excited that you're interested in contributing to the elekto software! Check out the resources below to get started.

Please refer to [CONTRIBUTING](CONTRIBUTING.md) for more information on how to best contributed to contribute to elekto.

# Support
Your help and feedback is always welcome!

If you find an issue let us know, either by clicking the Create Issue on any of the website pages, or by directly opening an issue [here](https://github.com/elekto-io/elekto/issues/new) in the repo.